install:
	pipenv install --ignore-pipfile

run:
	pipenv run uvicorn app.main:app --host 0.0.0.0 --port 3333 --reload

run-database:
	supabase start

run-migration:
	supabase migration up
