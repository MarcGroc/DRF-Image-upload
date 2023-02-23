poetry run python manage.py check_db
poetry run python manage.py makemigrations --noinput
poetry run python manage.py migrate --noinput
poetry run python manage.py check_or_create_user
poetry run python manage.py runserver 0.0.0.0:8000