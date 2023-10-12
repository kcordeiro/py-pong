PROJECT = py_pong

.PHONY: help clean dev ready source wheel build

# Auto documented Makefile:
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
#
# This is first so doing "make" without an argument does "make help"
help: ## List Makefile targets
	$(info Makefile documentation)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-10s\033[0m %s\n", $$1, $$2}'

clean:  ## Delete local builds and cached files
	rm -rf ./.mypy_cache
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./*.egg-info

dev:  ## Create local dev environment
	poetry install --sync
	poetry run pre-commit install

ready: clean ## Run linting and mypy
	poetry run pre-commit run -a
	poetry run pylint ./$(PROJECT)
	poetry run mypy ./$(PROJECT)

source: ## Build source distribution package
	poetry build --format sdist

wheel: ## Build binary wheel distribution package
	poetry build --format wheel

build: wheel source; ## Build all distribution packages
