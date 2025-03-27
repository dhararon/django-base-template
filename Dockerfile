# define an alias for the specfic python version used in this file.
FROM python:3.12

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

RUN pip install -U pip uv

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_HOME = /app
ENV POETRY_VIRTUALENVS_CREATE 0

WORKDIR ${APP_HOME}

# Install dependencies
COPY ./pyproject.toml ${WORKDIR}
RUN uv pip install -r pyproject.toml --system

COPY ./docker/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# copy application code to WORKDIR
COPY ./src ${APP_HOME}

ENTRYPOINT ["/entrypoint"]
