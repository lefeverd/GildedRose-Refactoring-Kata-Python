.PHONY: init test coverage

all: init

init:
	python3 -m venv ./venv
	./venv/bin/pip install -r requirements.txt

test:
	./venv/bin/python -m unittest tests/test*

coverage:
	./venv/bin/coverage run -m unittest tests/test* && ./venv/bin/coverage html
