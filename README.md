# Django Template

Django template is a whitelabel project for build applications in the easy way.

## Requirements
- Docker
- Docker compose
- Make

## How to start
1. First that all you need to change the env files into .envs directory
2. Then you have to run the next make command

```bash
$ make setup
```
### Run admin configuration

1. First you need to create and super admin user

```bash
$ make useradmin
```

2. Then just need to run the server with

```bash
$ make admin
```

NOTE: If you change some docker or docker-compose configuration you must to apply `make build` command for load the changes.

### Run api configuration

1. Just need to run the next command

```bash
$ make api
```

# Useful make commands
`setup`: Run all configuration for the first time.

`build`: Add docker or docker composer configurations to local image construction.

`rebuild`: Build all the images without cache.

`down`: Delete all images creates.

`api`: Run API server with postgres server

`admin`: Run Admin server with postgres server

`db`: Run Postgres database server

`recreate`: Delete all database configuration and rebuild it

`migrations`: Shortcut for ./manage.py makemigrations

`migrate`: shortcut for ./manage.py migrate

`useradmin`: Create an super user admin into django

`grant_admin`: Grant admin permissions to one user based on email. You need to specify the `EMAIL` variable into the environment or run `EMAIL=<email> make grant_admin`

`grant_staff`: Grant staff permissions to one user based on email. You need to specify the `EMAIL` variable into the environment or run `EMAIL=<email> make grant_staff`

`mailhog`: Run email server

`validate`: Run the pre-commit command for scan all files.

`update`: Run pre-commit plugins, pip, poetry and poetry dependencies.

# Dependencies

## Global

[psycopg](https://pypi.org/project/psycopg/): Psycopg 3 is a modern implementation of a PostgreSQL adapter for Python.

[django-configurations](https://django-configurations.readthedocs.io/en/stable/patterns.html): django-configurations eases Django project configuration by relying on the composability of Python classes. It extends the notion of Django’s module based settings loading with well established object oriented programming patterns.

[python-dotenv](https://pypi.org/project/python-dotenv/): Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. It helps in the development of applications following the 12-factor principles.

[django-anymail](https://pypi.org/project/django-anymail/): Anymail lets you send and receive email in Django using your choice of transactional email service providers (ESPs). It extends the standard django.core.mail with many common ESP-added features, providing a consistent API that avoids locking your code to one specific ESP.

[django-model-utils](https://pypi.org/project/django-model-utils/): Django model mixins and utilities.

[djangorestframework](https://pypi.org/project/djangorestframework/): Awesome web-browsable Web APIs.

[django-cors-headers](https://pypi.org/project/django-cors-headers/): A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.

[drf-spectacular](https://pypi.org/project/drf-spectacular/): Sane and flexible OpenAPI 3 schema generation for Django REST framework

[django-structlog](https://django-structlog.readthedocs.io/en/latest/): Logging will then produce additional cohesive metadata on each logs that makes it easier to track events or incidents.

[django-allauth](https://pypi.org/project/django-allauth/): Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.


## Development Group
[pylint-django](https://pypi.org/project/pylint-django/): pylint-django is a Pylint plugin for improving code analysis when analysing code using Django. It is also used by the Prospector tool.

[pytest](https://pypi.org/project/pytest/): The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

[django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/): The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.

[werkzeug](https://pypi.org/project/Werkzeug/): The comprehensive WSGI web application library.

[django-extensions](https://pypi.org/project/django-extensions/): Django Extensions is a collection of custom extensions for the Django Framework.

[pytest-django](https://pypi.org/project/pytest-django/): A Django plugin for pytest.

# MailHog Server to Development

To run Mailhog, you only need to create the following `.env-server-email` variable file within the .envs folder and add the following variables:

- EMAIL_HOST
- EMAIL_PORT
- EMAIL_BACKEND
- EMAIL_USE_TLS

Mailhog runs when you execute `make api` or `make admin`, for local development environment only.
