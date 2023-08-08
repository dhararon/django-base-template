ARG PYTHON_VERSION=3.11
ARG BUILD_ENVIRONMENT
ARG APP_HOME=/app

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION}

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip poetry

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

# Install dependencies
COPY ./pyproject.toml /tmp

RUN cd /tmp && poetry config virtualenvs.create false \
  && poetry install


COPY ./docker/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# copy application code to WORKDIR
COPY ./src ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
