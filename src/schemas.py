from marshmallow import fields, validate
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .models import Book


class BookSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Book
        load_instance = True

    serial_number = fields.String(required=True, validate=validate.Length(equal=6))
    title = fields.String(required=True, validate=validate.Length(min=1))
    author = fields.String(required=True, validate=validate.Length(min=1))
    is_checked_out = fields.Boolean()
    checked_out_by = fields.String(validate=validate.Length(equal=6))
    checked_out_date = fields.DateTime()


book_schema = BookSchema()
books_schema = BookSchema(many=True)
