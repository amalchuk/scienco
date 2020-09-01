.PHONY: all install pip-update-setuptools pip-install-development install-development build test coverage clean

all: install

install:
	@echo "Installing the package"
	@python setup.py install

pip-update-setuptools:
	@echo "Updating the pip, setuptools and wheel packages"
	@python -m pip install pip setuptools wheel --upgrade --force-reinstall --no-cache-dir

pip-install-development: pip-update-setuptools
	@echo "Installing the dependencies for development"
	@pip install --requirement requirements-dev.txt --upgrade --force-reinstall --no-cache-dir

install-development: pip-install-development
	@echo "Installing the package in the development mode"
	@python setup.py develop

build:
	@echo "Building the package"
	@python setup.py build bdist_wheel sdist

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
