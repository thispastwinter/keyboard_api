install:
	pipenv install --ignore-pipfile

install-dev:
	pipenv install --dev --ignore-pipfile

format:
	pipenv run black .

run:
	pipenv run uvicorn app.main:app --host 0.0.0.0 --port 3333 --reload

run-database:
	supabase start

run-migration:
	supabase migration up

test:
	pipenv run pytest

test-verbose:
	pipenv run pytest -s -vv

typecheck:
	pipenv run mypy app/main.py
	
lint-format:
	pipenv run black --check ./app

ci: test lint-format typecheck

