.PHONY: all install build install-development test coverage clean

all: install

install:
	@echo "Installing the package"
	@python setup.py install

build:
	@echo "Building the package"
	@python setup.py build bdist_wheel sdist

install-development:
	@echo "Installing the package in the development mode"
	@pip install --editable .[dev] --upgrade --force-reinstall --quiet --no-cache-dir

test:
	@echo "Running the test cases"
	@coverage run -m pytest

coverage: test
	@echo "Analyzing the code coverage for all test cases"
	@coverage report
	@coverage html

clean:
	@echo "Delete all temporary files"
	@find scienco tests -type f -name '*.py[cod]' | xargs rm --force
	@find scienco tests -type d -name '__pycache__' | xargs rm --force --recursive
