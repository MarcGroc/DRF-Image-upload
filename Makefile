default: format

format:
	echo "Formatting"
	black ./rest_api
	isort ./rest_api
	echo "Formatted successfully"

lint:
	echo "Linting"
	flake8 ./rest_api
	echo "Linted successfully"

run-local:
	echo "Running application with db connection check"
	python manage.py check_db && python manage.py runserver

tests:
	echo "Running tests"
	python manage.py test

checkmigrations:
	echo "Checking migrations for errors"
	python manage.py makemigrations --check --no-input --dry-run

migrations:
	echo "Making app migrations"
	python manage.py makemigrations
	echo "Making app migrate"
	python manage.py migrate

# Docker commands
build-backend:
	docker build . -f deployment/backend/Dockerfile -t backend

#build-task-runner:
#	docker build . -f deployment/task_runner/Dockerfile -t task-runner
#
#docker-compose:
#	docker-compose -f docker-compose.development.yml rm -s -v -f
#	docker-compose -f docker-compose.development.yml up --build

