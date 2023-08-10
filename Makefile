.DEFAULT_GOAL := help

DOCKER_COMPOSE_FILE = docker-compose.yml

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# General
.PHONY: setup
setup: ## Setup the project
	@sh scripts/setup

# Docker
.PHONY: build
build: ## Build or rebuild project
	@docker compose -f ${DOCKER_COMPOSE_FILE} build

.PHONY: rebuild
rebuild: ## Build with no cache option
	@docker compose -f ${DOCKER_COMPOSE_FILE} build --no-cache

.PHONY: down
down: ## Stop project
	@docker compose -f ${DOCKER_COMPOSE_FILE} down bash

.PHONY: bash
bash: ## Start bash project
	@docker compose -f ${DOCKER_COMPOSE_FILE} up -d bash && docker compose -f ${DOCKER_COMPOSE_FILE} exec bash zsh
