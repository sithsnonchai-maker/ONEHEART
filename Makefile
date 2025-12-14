PY?=python3

.PHONY: install test

install:
	$(PY) -m pip install -e .

test:
	$(PY) -m pytest -q
