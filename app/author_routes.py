from app import db
from app.models.author import Author
from app.models.book import Book
from app.book_routes import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")