# Tutorial-Authentication-Flask-API-live-82
Tutorial made from 'Live de Python #82 - Autenticação de uma API Flask' (Eduardo Mendes) by Marcus Mariano 

---

## Introduction

Authentication Flask API

Packages

- flask
- flask-sqlalchemy
- flask-migrate
- flask-marshmallow
- marshmallow-sqlalchemy
- passlib
- flask_jwt_extended

Dev-packages

- requests
- ipdb

---

## Installation

```sh

pipenv install --dev

```

---

## How to Run

Config App

```sh

export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run

```

Creat DB
Make Magrations 
```sh
flask db init 

flask db migrate

flask db upgrade
```

---

## Tests

Testing Flask API
```sh

python -m unittest -v tests/tests_flask_api.py

```

Run Coverage
```sh

coverage run --source=app -m unittest discover -s tests

```

Run Coverage and unittest with verbose mode
```sh

pipenv run coverage run --source=app -m unittest discover -s tests -v

```

Run Coverage Report
```sh

coverage report

```

Run Coverage generate HTML report
```sh

coverage html

```

---

## License

Code and documentation are available according to the GNU GENERAL PUBLIC LICENSE Version 3 (see [LICENSE](https://www.gnu.org/licenses/gpl.html)).
