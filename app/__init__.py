"""
Authentication Flask API

Tutorial-Authentication-Flask-API-live-82

Homepage and documentation:


License: GNU GENERAL PUBLIC LICENSE Version 3

"""

from flask import Flask
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .model import configure as config_db
from .serealizer import configure as config_ma
from .books import bp_books
from .user import bp_user 
from .login import bp_login


def create_app():
    """Create app method - Application Factorie. Return initial state of app"""
    
    # configure app
    app = Flask(__name__)

    # configure SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudzin.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # congigure flask_jwt_extended
    app.config['JWT_SECRET_KEY'] = 'Batatinhas voadoras são melhor que eu'

    # configure DB and serealiser
    config_db(app)
    config_ma(app)

    # configure Migrations
    Migrate(app, app.db)

    # Ripper no banco ????
    JWTManager(app)

    # Register Blueprints
    app.register_blueprint(bp_books)
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_login)

    return app
