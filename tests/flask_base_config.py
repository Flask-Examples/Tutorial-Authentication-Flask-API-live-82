"""Basic config for Tests."""

from json import loads
from unittest import TestCase
from app import create_app
from flask import url_for


class TestFlaskBase(TestCase):
    """Class Base for Test."""

    def setUp(self):
        """
        Fixture do method - Method setup
        Run before all tests.
        """
        self.app = create_app()
        self.app.testing = True
        self.app_context = self.app.test_request_context()
        self.app_context.push()
        self.client = self.app.test_client()
        self.app.db.create_all()
        self.user = {
            'username': 'test',
            'password': '1234'
        }


    def tearDown(self):
        """
        Fixture do method - Method setup
        Run after all tests.
        """
        self.app.db.drop_all()


    def create_user(self):
        """Test."""

        self.client.post(url_for('user.register'), json=self.user)


    def generate_token(self):
        """Test."""
        login = self.client.post(url_for('login.login'), json=self.user)

        return {
            'Authorization': 'Bearer ' + loads(login.data.decode())['access_token']
        }
