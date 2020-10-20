.PHONY: all install install-development build upload docs test coverage clean

all: install clean

install:
	@echo "Installing the package"
	@poetry install --no-dev --quiet --no-interaction

install-development:
	@echo "Installing the package in the development mode"
	@poetry install --no-root --quiet --no-interaction

build:
	@echo "Building the package"
	@poetry build --format sdist --quiet --no-interaction

upload:
	@echo "Upload to the package registry"
	@poetry publish --quiet --no-interaction

docs:
	@echo "Build the documentation"
	@poetry run mkdocs build --clean

test:
	@echo "Running the test cases"
	@poetry run coverage run -m pytest --exitfirst --quiet

coverage: test
	@echo "Analyzing the code coverage for all test cases"
	@poetry run coverage report

clean:
	@echo "Delete all temporary files"
	@find scienco tests -type f -name '*.py[cod]' | xargs rm --force
	@find scienco tests -type d -name '__pycache__' | xargs rm --force --recursive
