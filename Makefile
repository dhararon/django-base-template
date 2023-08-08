.DEFAULT_GOAL := help

DOCKER_COMPOSE_FILE = docker-compose.yml

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# General
.PHONY: setup
setup: ## Setup the project
	@sh scripts/setup && make update

.PHONY: update
update: ## Update all dependencies
	@sh scripts/update

# Docker
.PHONY: build
build: ## Build or rebuild project
	@docker compose -f ${DOCKER_COMPOSE_FILE} build

.PHONY: rebuild
rebuild: ## Build with no cache option
	@docker compose -f ${DOCKER_COMPOSE_FILE} build --no-cache

.PHONY: down
down: ## Delete all images
	@docker compose -f ${DOCKER_COMPOSE_FILE} down

# Web services
.PHONY: admin
admin: ## Start admin project
	@docker compose -f ${DOCKER_COMPOSE_FILE} up admin

.PHONY: api
api: ## Start api project
	@docker compose -f ${DOCKER_COMPOSE_FILE} up api

# Databases
.PHONY: db
db: ## Run postgres
	@docker compose -f ${DOCKER_COMPOSE_FILE} up postgres

.PHONY: recreate
recreate: ## Delete and recreate postgres image
	@docker compose -f ${DOCKER_COMPOSE_FILE} up -d --build --force-recreate --renew-anon-volumes postgres

.PHONY: migrations
migrations: ## Create migrations
	@docker compose -f ${DOCKER_COMPOSE_FILE} run admin python manage.py makemigrations

.PHONY: migrate
migrate: ## Excecute migrations
	@docker compose -f ${DOCKER_COMPOSE_FILE} run admin python manage.py migrate


# Application
.PHONY: useradmin
useradmin: ## Create super user into the app
	@docker compose -f ${DOCKER_COMPOSE_FILE} run admin python manage.py createsuperuser

.PHONY: grant_admin
grant_admin: ## Grant admin privileges to user by email
	@docker compose -f ${DOCKER_COMPOSE_FILE} run admin python manage.py superuser ${EMAIL}

.PHONY: grant_staff
grant_staff: ## Grant staff privileges to user by email
	@docker compose -f ${DOCKER_COMPOSE_FILE} run admin python manage.py staff ${EMAIL}

# Email
.PHONY: mailhog
mail: ## Start mailhog server
	@docker compose -f ${DOCKER_COMPOSE_FILE} up mailhog

# Pre commit
.PHONY: validate
validate: ## Run precommit for all files
	@pre-commit run --all-files
