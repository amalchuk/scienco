.PHONY: all install pip-update-setuptools pip-install-development update test coverage clean

all: install test clean

install:
	@echo "Installing the dependencies"
	@poetry install --no-root --quiet --no-interaction

pip-update-setuptools:
	@echo "Updating the pip, setuptools and wheel packages"
	@python -m pip install pip setuptools wheel --upgrade --force-reinstall --no-cache-dir

pip-install-development: pip-update-setuptools
	@echo "Installing the dependencies for development"
	@pip install --requirement requirements-dev.txt --no-deps --upgrade --require-hashes --quiet --no-cache-dir

update:
	@echo "Downloading the latest versions of the dependencies"
	@poetry update --lock --quiet --no-interaction
	@poetry export --format requirements.txt --output requirements-dev.txt --dev

test:
	@echo "Running the test cases"
	@coverage run -m pytest --quiet

coverage: test
	@echo "Analyzing the code coverage for all test cases"
	@coverage report
	@coverage html

clean:
	@echo "Delete all temporary files"
	@find scienco tests -type f -name '*.py[cod]' | xargs rm --force
	@find scienco tests -type d -name '__pycache__' | xargs rm --force --recursive
