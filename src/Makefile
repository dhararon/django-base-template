.DEFAULT_GOAL := help

DOCKER_COMPOSE_FILE = docker-compose.yml

.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# General
.PHONY: setup
setup: ## Setup the project
	@sh ../scripts/python-setup

# Pre commit
.PHONY: fmt
fmt: ## Run precommit for all files
	@pre-commit run --all-files
