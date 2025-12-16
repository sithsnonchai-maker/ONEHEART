# ONEHEART
If you are hoping to profit from this, you are on the wrong path. But if you want to help your fellow human beings, you are on the right path.

## Quickstart

1. Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install the project in editable mode and run tests:

```bash
pip install -e .
pytest -q
```

3. Run the tiny CLI to see the greeting:

```bash
python -m oneheart.cli
```

## Development

To set up a development environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pre-commit install
pre-commit run --all-files
```

This repository was scaffolded from the existing metadata in this workspace.
