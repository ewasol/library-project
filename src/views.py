from sqlalchemy import exc

from .run import db

from flask import Blueprint, request, Response, jsonify
from .models import Book
from .schemas import book_schema, books_schema
from datetime import datetime

bp = Blueprint('bp', __name__)


@bp.route('/books', methods=['GET'])
def get_books() -> tuple[Response, int]:
    books = Book.query.all()
    return jsonify(books_schema.dump(books)), 200


@bp.route('/books', methods=['POST'])
def add_book() -> tuple[Response, int]:
    data = request.json
    if errors := book_schema.validate(data, session=db.session):
        return jsonify(errors), 400

    try:
        new_book = book_schema.load(data, session=db.session)
        db.session.add(new_book)
        db.session.commit()
    except exc.DBAPIError:
        db.session.rollback()
        return jsonify(
            {'error': 'A book with this serial number already exists.'}
        ), 409

    return jsonify(book_schema.dump(new_book)), 201


@bp.route('/books/<serial_number>', methods=['DELETE'])
def delete_book(serial_number: int) -> tuple[Response, int]:
    if book := Book.query.filter_by(serial_number=serial_number).first():
        db.session.delete(book)
        db.session.commit()
        return jsonify({'message': 'Book deleted'}), 200
    return jsonify({'message': 'Book not found'}), 404


@bp.route('/books/<serial_number>', methods=['PUT'])
def update_book(serial_number: int) -> tuple[Response, int]:
    if not (book := Book.query.filter_by(serial_number=serial_number).first()):
        return jsonify({'message': 'Book not found'}), 404

    data = request.json

    if errors := book_schema.validate(data, session=db.session):
        return jsonify(errors), 400

    is_checked_out = data.get('is_checked_out', None)
    if is_checked_out is None:
        return jsonify({'error': 'Invalid data provided'}), 400

    book.is_checked_out = is_checked_out
    if is_checked_out:
        book.checked_out_by = data.get('checked_out_by')
        book.checked_out_date = datetime.now()
    else:
        book.checked_out_by = None
        book.checked_out_date = None

    db.session.commit()

    return jsonify(book_schema.dump(book)), 200
