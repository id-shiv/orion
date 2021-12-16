ifneq (,$(wildcard ./.env))
	include .env
	export
	ENV_FILE_PARAM = --env-file .env
endif

build:
	docker compose up --build -d --remove-orphans

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs

migrate:
	docker compose exec api python manage.py migrate

makemigrations:
	docker compose exec api python manage.py makemigrations

superuser:
	docker compose exec api python manage.py createsuperuser

down-v:
	docker compose down -v

volume:
	docker volume inspect orion_postgres_data

postgres-db:
	docker compose exec postgres-db psql --username=admin --dbname=orion

test:
	docker compose exec api pytest -p no:warnings --cov=.

test-html:
	docker compose exec api pytest -p no:warnings --cov=. --cov-report html