from app import db
from app.models.author import Author
from app.models.book import Book
from app.models.genre import Genre
from app.book_routes import validate_model
from flask import Blueprint, jsonify, abort, make_response, request

genres_bp = Blueprint("genres_bp", __name__, url_prefix="/genres")