.PHONY: all install build install-development upload docs test coverage clean

all: install clean

install:
	@echo "Installing the package"
	@python setup.py install --quiet

build:
	@echo "Building the package"
	@python setup.py build bdist_wheel sdist

install-development:
	@echo "Installing the package in the development mode"
	@python -m pip install pip setuptools wheel --upgrade --quiet --no-cache-dir
	@python setup.py develop --quiet
	@python -m pip install --requirement requirements-dev.txt --upgrade --quiet --no-cache-dir

upload: build
	@echo "Upload package to a PyPI"
	@find dist -type f | xargs twine upload --disable-progress-bar

docs:
	@echo "Build the documentation"
	@mkdocs build --clean

test:
	@echo "Running the test cases"
	@coverage run -m pytest

coverage: test
	@echo "Analyzing the code coverage for all test cases"
	@coverage report

clean:
	@echo "Delete all temporary files"
	@find scienco tests -type f -name '*.py[cod]' | xargs rm --force
	@find scienco tests -type d -name '__pycache__' | xargs rm --force --recursive
