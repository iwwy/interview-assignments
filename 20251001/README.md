# Assignment Project

## Installation

Install the application with the following commands:

```bash
python -m venv task
cd task
. bin/activate
pip install poetry
git clone https://github.com/iwwy/task20251001.git
cd task20251001
poetry install
```

Change to the application directory:

```bash
cd src/webapp/app/
```

## Usage

Run the development server with the following command in the application directory:

```bash
poetry run python manage.py runserver
```

The application is available at [http://localhost:8000](http://localhost:8000).

Run the tests with the following command in the application directory:

```bash
poetry run black assignment
poetry run mypy assignment
poetry run flake8 assignment
poetry run python manage.py test
```
