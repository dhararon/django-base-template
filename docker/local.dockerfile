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

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

#ADD "https://www.random.org/cgi-bin/randbyte?nbytes=10&format=h" skipcache

USER $USER_NAME
# terminal colors with xterm
ENV TERM xterm

RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t https://github.com/denysdovhan/spaceship-prompt \
    -a 'SPACESHIP_PROMPT_ADD_NEWLINE="false"' \
    -a 'SPACESHIP_PROMPT_SEPARATE_LINE="false"' \
    -p git \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions

WORKDIR /app
