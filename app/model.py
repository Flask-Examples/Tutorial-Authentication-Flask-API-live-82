"""Model for database."""

from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256 as hash256


db = SQLAlchemy()

def configure(app):
    """Create app."""
    db.init_app(app)
    app.db = db


class Book(db.Model):
    """Create DB."""
    id = db.Column(db.Integer, primary_key=True)
    livro = db.Column(db.String(255))
    escritor = db.Column(db.String(255))


class User(db.Model):
    """Create Users."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)


    def gen_hash(self):
        """Create Hash."""
        self.password = hash256.hash(self.password)


    def verify_password(self, password):
        """Verify Hash password."""
        return hash256.verify(password, self.password)
