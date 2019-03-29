"""Login."""

from datetime import timedelta
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import create_access_token, create_refresh_token
from .model import User
from .serealizer import UserSchema


bp_login = Blueprint('login', __name__)


@bp_login.route('/login', methods=['POST'])
def login():
    """Blueprint login user."""

    user, error = UserSchema().load(request.json)

    if error:
        return jsonify(error), 401

    user = User.query.filter_by(username=user.username).first()

    if user and user.verify_password(request.json['password']):
        access_token = create_access_token(
            identity=user.id,
            expires_delta = timedelta(seconds=1)
        )
        refresh_token = create_refresh_token(identity=user.id)

        return  jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'message': 'Success'
        }), 200
    return jsonify({
        'message': 'Bad Credentials'
    }), 401
