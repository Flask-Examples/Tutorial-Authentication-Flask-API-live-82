"""Tests flask API.
"""

from flask import url_for
from flask_base_config import TestFlaskBase
from time import sleep


class TestCadastro(TestFlaskBase):
    """Class TestCadastro - inherits of TestFlaskBase."""

    def test_cadastrar_must_be_return_a_payload_sent_without_id(self):
        """Test Cadastrar."""
        dado = {
            'escritor': 'Marcus',
            'livro': 'Python 3'
        }

        response = self.client.post(url_for('books.cadastrar'), json=dado)

        # Verify response.json
        # import ipdb; ipdb.set_trace()

        response.json.pop('id')

        self.assertEqual(dado, response.json)


    def test_cadastrar_must_be_return_error_when_payload_is_incomplete(self):
        """Test Cadastrar."""
        dado = {
            'livro': 'Python 3'
        }

        esperado = {'escritor': ['Missing data for required field.']}
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        # Verify response.json
        # import ipdb; ipdb.set_trace()

        # response.json.pop('id')

        self.assertEqual(esperado, response.json)


    def test_cadastrar_must_be_return_error_when_payload_had_id_key(self):
        """Test Cadastrar."""
        dado = {
            'id': 1,
            'escritor': 'Marcus',
            'livro': 'Python 3'
        }

        esperado = {'id': ['Não envie pelo amor de Deus o ID.']}
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        self.assertEqual(esperado, response.json)


class TestMostrar(TestFlaskBase):
    """Class TestMostrar - inherits of TestFlaskBase."""

    def test_mostrar_must_be_return_a_empty_query(self):
        """Test mostrar empty query ."""

        self.create_user()
        token = self.generate_token()

        # Failure test because time of token validation is more than 1 second.
        # sleep(2)

        response = self.client.get(url_for('books.mostrar'), headers=token)

        self.assertEqual([], response.json)


    def test_mostrar_must_be_return_a_empty_with_inserted_element(self):
        """Test mostrar empty query ."""

        dado = {
            'escritor': 'Marcus',
            'livro': 'Python 3'
        }

        self.create_user()
        token = self.generate_token()

        response = self.client.post(url_for('books.cadastrar'), json=dado)
        response = self.client.post(url_for('books.cadastrar'), json=dado)

        response = self.client.get(url_for('books.mostrar'), headers=token)

        self.assertEqual(2, len(response.json))


class TestDeletar(TestFlaskBase):
    """Class TestDeletar - inherits of TestFlaskBase."""

    def test_deletar_must_be_return_deleted_when_dont_find_out_register(self):
        """Test Deletar empty query ."""

        response = self.client.get(url_for('books.deletar', identificador=1))

        self.assertEqual(response.json, 'Deletado!!!!')


    def test_deletar_must_be_return_deleted_when_find_out_register_in_db(self):
        """Test Deletar empty query ."""

        dado = {
            'escritor': 'Marcus',
            'livro': 'Python 3'
        }

        response = self.client.post(url_for('books.cadastrar'), json=dado)

        response = self.client.get(url_for('books.deletar', identificador=1))

        self.assertEqual(response.json, 'Deletado!!!!')


class TestModificar(TestFlaskBase):
    """Class TestModificar - inherits of TestFlaskBase."""

    def test_modificar_must_be_return_deleted_when_dont_find_out_register(self):
        """Test Modificar empty query ."""

        identificador = 1

        esdado_inicial = {
            'escritor': 'Marcus',
            'livro': 'Python 3'
        }

        esdado_final = {
            'escritor': 'Marcus',
            'livro': 'Python 2'
        }

        self.client.post(url_for('books.cadastrar'), json=esdado_inicial)

        response = self.client.post(url_for('books.modificar', identificador=1), json=esdado_final)

        # Verify response.json
        # import ipdb; ipdb.set_trace()

        self.assertEqual(esdado_final['livro'], response.json['livro'])

        self.assertEqual(identificador, response.json['id'])
