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

### Docker Compose Environment Variables
Create a .env file and add this variables.

```
# Docker Compose
ENVIRONMENT=local
APP_API_PORT=8080
APP_ADMIN_PORT=8081
DB_PORT=5432
MAILHOG_PORT_1=8025
MAILHOG_PORT_2=1025
```

### Environment Variables
For local environment you need to follow this steps:

1. Create a .envs folder into root path
2. Create a folder called `local` the name must be equals to the ENVIRONMENT variable value describe above.
3. Create a `.env-django` file
4. Create a `.env-postgres` file

`.env-django` content:
```
DJANGO_CONFIGURATION=LocalConfig
DJANGO_DEBUG=True
DJANGO_SECRET_KEY=<<YOUR SECRET KEY>>
```
`.env-postgres` content:
```
DJANGO_POSTGRES_HOST=postgres
DJANGO_POSTGRES_PORT=5432
DJANGO_POSTGRES_DB=app
DJANGO_POSTGRES_USER=root
DJANGO_POSTGRES_PASSWORD=toor
```

# Run environment

## Run migrations
For run migrations just execute this command

```bash
$ make migrate
```

## Load superuser data
After run migrations you have to create a super user, so you can use djang's superuser command or load the fixture with this command:

```bash
$ make loaddata
```

## Run the server
Finally you can run the admin server with this command:

```bash
$ make admin
```

# Useful make commands
`setup`: Run all configuration for the first time.

`build`: Add docker or docker composer configurations to local image construction.

`rebuild`: Build all the images without cache.

`admin`: Run Admin server with postgres server

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


## Development Group
[pylint-django](https://pypi.org/project/pylint-django/): pylint-django is a Pylint plugin for improving code analysis when analysing code using Django. It is also used by the Prospector tool.

[pytest](https://pypi.org/project/pytest/): The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

[django-debug-toolbar](https://pypi.org/project/django-debug-toolbar/): The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel’s content.

[werkzeug](https://pypi.org/project/Werkzeug/): The comprehensive WSGI web application library.

[django-extensions](https://pypi.org/project/django-extensions/): Django Extensions is a collection of custom extensions for the Django Framework.

[pytest-django](https://pypi.org/project/pytest-django/): A Django plugin for pytest.
