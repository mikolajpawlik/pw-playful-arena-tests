# pw-playful-arena-tests

![Tests](https://github.com/mikolajpawlik/pw-playful-arena-tests/actions/workflows/tests.yml/badge.svg)

Playwright E2E tests for [pw-playful-arena](https://pw-playful-arena.lovable.app) PWA.

## Stack

- Python 3.12+
- [pytest-playwright](https://playwright.dev/python/)

## Setup

```bash
python -m venv .venv
.venv\Scripts\pip install -e ".[dev]"
.venv\Scripts\playwright install
```

## Running tests

```bash
# chromium + firefox (default)
.venv\Scripts\pytest

# mobile (Pixel 5)
.venv\Scripts\pytest --browser chromium --device "Pixel 5" -o addopts=""
```
