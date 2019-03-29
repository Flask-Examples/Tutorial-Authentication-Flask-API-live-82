"""Tests Authetication."""

from flask import url_for
from flask_base_config import TestFlaskBase


class TestLogin(TestFlaskBase):
    """Class for Test Login."""

    def test_api_must_be_generate_token(self):
        """Test Login - generate token."""
        self.create_user()
        login = self.client.post(url_for('login.login'), json=self.user)
        
        # Verify login.json
        # import ipdb; ipdb.set_trace()

        esperado = ['access_token', 'message', 'refresh_token']

        self.assertEqual(list(login.json.keys()), esperado)

    def test_login_must_be_return_error_when_login_is_incomplete(self):
        """Test when login is incomplete."""

        dado = {
            'username': ''
        }

        response = self.client.post(url_for('login.login'), json=dado)

        # Verify response.json
        # import ipdb; ipdb.set_trace()

        esperado = {
            'password': ['Missing data for required field.']        
        }

        self.assertEqual(esperado, response.json)

    def test_login_must_be_return_error_when_login_is_bad_credentials(self):
        """Test when login is bad credentials."""

        dado = {
            'password': '1234',
            'username': 'eu'
        }

        response = self.client.post(url_for('login.login'), json=dado)

        # Verify response.json
        # import ipdb; ipdb.set_trace()

        esperado = {
            'message': 'Bad Credentials'
        }

        self.assertEqual(response.json, esperado)
