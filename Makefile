PY?=python3

.PHONY: install test dev

install:
	$(PY) -m pip install -e .

dev:
	$(PY) -m pip install -e .[dev]

test:
	$(PY) -m pytest -q
