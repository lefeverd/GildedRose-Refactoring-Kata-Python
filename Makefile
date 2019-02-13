.PHONY: init test coverage

all: init

init:
	python3 -m venv ./venv
	./venv/bin/pip install -r requirements.txt

test:
	./venv/bin/python test_*

coverage:
	./venv/bin/coverage run test_* && ./venv/bin/coverage html
