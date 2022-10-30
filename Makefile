run:
	poetry run python manage.py runserver

get_requirements:
	poetry export --without-hashes > requirements.txt

make_messages:
	django-admin makemessages -l ru

compile_messages:
	django-admin compilemessages -l ru
