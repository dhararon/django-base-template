# Global variables
BASE_DIR := $(dir $(lastword $(MAKEFILE_LIST)))
DOCKER_COMPOSE_FILE = ./docker-compose.yml

.DEFAULT_GOAL := help

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# ------------------------------------------- Docker commands ------------------------------------------
.PHONY: build
build: ## [Docker] Build or rebuild project
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} build

.PHONY: rebuild
rebuild: ## [Docker] Build with no cache option
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} build --no-cache

.PHONY: down
down: ## [Docker] Delete all images
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} down

# ------------------------------------------- Setup commands ------------------------------------------

.PHONY: init
init: ## Start the project configuration
	@sh docker/setup \
	&& curl https://raw.githubusercontent.com/dhararon/branch-color/refs/heads/main/install.sh --output /tmp/install-branch-color.sh
	/bin/bash /tmp/install-branch-color.sh \
	&& make db && make migrate && make loaddata \
	&& clear && echo "Your email for django admin access is: dharwin@codelovers.club and password: admin123"

# ------------------------------------------- Coding commands ------------------------------------------
# Pre commit
.PHONY: validate
validate: ## [General] Run precommit for all files
	@pre-commit run --all-files

# TODO: Use a container for execute this command
# UPDATE
.PHONY: update
update: ## [General] Update all dependencies
	@echo "Updating pre-commit plugins ..." \
	&& pre-commit autoupdate \
	&& echo "Updating pip and uv ..." \
	&& pip install -U pip uv \
	&& echo "Updating uv dependencies ..." \
	&& uv sync --upgrade

# ------------------------------------------- Database commands ------------------------------------------

.PHONY: db
db: ## [Database] Run postgres
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} up -d postgres

.PHONY: db-recreate
db-recreate: ## [Database] Delete and recreate postgres image
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} stop postgres \
	&& BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} rm -sf postgres \
	&& BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} down -v \
	&& BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} up -d postgres \
	&& BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py migrate

.PHONY: dumpdata
dumpdata: ## [Database] Dumpdata for fixtures
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py dumpdata users --format=json > ./src/fixtures/users.json

.PHONY: loaddata
loaddata: ## [Database] Load for fixtures
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py loaddata --format=json fixtures/users.json

# ------------------------------------------- Django commands ------------------------------------------

.PHONY: app
app: ## [Django] Start app project
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} up app

.PHONY: bash
bash: ## [Django] Start app project
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} up -d app && BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} exec app zsh

.PHONY: migrations
migrations: ## [Django] Create migrations
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py makemigrations

.PHONY: migrate
migrate: ## [Django] Excecute migrations
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py migrate

.PHONY: showmigrations
showmigrations: ## [Django] Show migrations
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py showmigrations

.PHONY: shell
shell: ## [Django] Init bash terminal
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} exec app sh

.PHONY: shell_plus
shell_plus: ## [Django] Init shell with superpowers
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py shell_plus

.PHONY: reset-migrations
reset-migrations: ## [Django] Delete all migrations files and create new one
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app find . -path "*/migrations/*.pyc"  -delete

# ------------------------------------------- Application commands -------------------------------------------

.PHONY: superadmin
superadmin: ## Create super user into the app
	@BASE_DIR=${BASE_DIR} docker compose -f ${DOCKER_COMPOSE_FILE} run app python manage.py createsuperuser
