ARG PYTHON_VERSION=3.11
ARG BUILD_ENVIRONMENT

# define an alias for the specfic python version used in this file.
FROM python:${PYTHON_VERSION}

# Install apt packages
RUN apt-get update && apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg dependencies
  libpq-dev \
  # Translations dependencies
  gettext \
  # zsh for development
  zsh \
  # vim
  vim \
  # curl
  curl \
  fonts-powerline \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

RUN pip install -U pip poetry poetry-plugin-up pre-commit

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

WORKDIR /app

# Copy dependencies
COPY ./pyproject.toml /app/pyproject.toml
RUN poetry config virtualenvs.create false \
  && poetry install

RUN git init && pre-commit install

#ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache


USER $USER_NAME
# terminal colors with xterm
ENV TERM xterm
# set the zsh theme
ENV ZSH_THEME agnoster
RUN apt-get update \
  && apt-get install -y zsh \
  && wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
