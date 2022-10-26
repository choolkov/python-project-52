run:
	poetry run python manage.py runserver

get_requirements:
	poetry export --without-hashes > requirements.txt
