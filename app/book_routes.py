from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)

    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 201)

@books_bp.route("", methods=["GET"])
def read_all_books():
    title_query = request.args.get("title")

    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()

    return jsonify([book.to_dict() for book in books])

@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_model(Book, book_id)
    return book.to_dict()

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_model(Book, book_id)

    request_body = request.get_json()
    book.update(request_body)

    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully updated"))

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_model(Book, book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully deleted"))