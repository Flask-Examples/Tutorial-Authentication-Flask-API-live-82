"""Serealizer."""

from flask_marshmallow import Marshmallow
from .model import Book, User
from marshmallow import fields, validates, ValidationError


ma = Marshmallow()

def configure(app):
    """Init serializer."""
    ma.init_app(app)


class BookSchema(ma.ModelSchema):
    """Create Book serializer."""
    class Meta():
        """Create serializer."""
        model = Book

    livro = fields.Str(required=True)
    escritor = fields.Str(required=True)


    @validates('id')
    def validate_id(self, value):
        """Validate Id."""
        raise ValidationError('Não envie pelo amor de Deus o ID.')


class UserSchema(ma.ModelSchema):
    """Create User serializer."""
    class Meta():
        """Create serializer."""
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)
