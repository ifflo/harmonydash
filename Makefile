# Makefile

# Python and Django management
PYTHON=python
PIP=pip
MANAGE=$(PYTHON) manage.py

# Virtual environment
VENV_NAME=venv
VENV_ACTIVATE=.$(VENV_NAME)/bin/activate
VENV_BIN=$(VENV_NAME)/bin

# Make sure commands are run inside the virtual environment
$(VENV_BIN)/%: $(VENV_NAME)
	@$(VENV_ACTIVATE) && $*

# Help target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Targets

setup: venv requirements migrate ## Set up the project after a fresh clone
venv: $(VENV_NAME)/bin/activate ## Create a virtual environment for the project
activate: ## Activate the virtual environment
	@echo "Activating virtual environment..."
	@$(VENV_ACTIVATE)
deactivate: ## Deactivate the virtual environment
	@echo "If the virtual environment is activated, deactivate it by typing 'deactivate'."
requirements: ## Install Python dependencies
	$(PIP) install -r requirements.txt
update-requirements: ## Update the requirements.txt file with the latest packages
	$(PIP) freeze > requirements.txt
migrate: ## Apply database migrations
	$(MANAGE) migrate
makemigrations: ## Create new migrations based on changes to models
	$(MANAGE) makemigrations
shell: ## Launch the Django shell
	$(MANAGE) shell
createsuperuser: ## Create a Django admin superuser
	$(MANAGE) createsuperuser
run: ## Run the Django development server
	$(MANAGE) runserver
celery: ## Run Celery worker (make sure RabbitMQ is running)
	celery -A harmonydash worker --loglevel=info
test: ## Run tests
	$(MANAGE) test app.tests
clean: ## Clean the project (remove cached files)
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.pyo' -delete
	find . -type d -name '__pycache__' -exec rm -rf {} +

.PHONY: help setup venv activate deactivate requirements update-requirements migrate makemigrations shell createsuperuser run celery test clean
