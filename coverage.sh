
pip install poetry

poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

coverage run --source=api -m pytest tests/

COVERALLS_REPO_TOKEN=4Z97eo3QPt2mW3wEx33xcTQhLwcyZUpFf coveralls
