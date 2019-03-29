"""Tests User."""

from flask import url_for
from flask_base_config import TestFlaskBase


class TestUserBP(TestFlaskBase):
    """Class for Test users."""

    def test_api_must_be_register_user_on_base(self):
        """Test register on base."""

        user = {
            'username': 'test',
            'password': '1234'
        }

        esperado = {
            'id': '1',
            'username': 'test',
            'password': ''
        }

        response = self.client.post(url_for('user.register'), json=user)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['username'], esperado['username'])


    def test_api_dont_must_be_register_user_on_base_when_lack_fields(self):
        """Test register error on base."""

        user = {
            'username': 'test'
        }

        esperado = {'password': ['Missing data for required field.']}
        response = self.client.post(url_for('user.register'), json=user)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, esperado)
