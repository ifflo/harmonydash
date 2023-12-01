# Makefile

# Define the manage.py command for convenience
MANAGE=python manage.py

run:
	@echo "Starting Django Server..."
	@$(MANAGE) runserver 8000

migrations:
	@echo "Making migrations..."
	@$(MANAGE) makemigrations

migrate:
	@echo "Applying migrations..."
	@$(MANAGE) migrate

shell:
	@echo "Opening Django Shell..."
	@$(MANAGE) shell

test:
	@echo "Running Tests..."
	@$(MANAGE) test

# You can add more commands as needed
