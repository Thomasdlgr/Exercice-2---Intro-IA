# AGENTS.md — OpenCode Session Guide

## Running tests

```
python -m pytest tests/ -v
```

No test framework config file exists — relies on plain `pytest` conventions.

## Issues are the source of truth

Bugs are documented in `issues/`, not in code comments. Fix them by reading the issue file first:

- **`issues/001-palindrome-bug.md`** — `is_palindrome()` in `toolbox/text_utils.py` doesn't strip spaces before comparison (line 3 has the bug annotation).
- **`issues/002-mutable-default-bug.md`** — `tag_reading()` in `toolbox/convert_utils.py` uses `tags: list = []` as a default argument, causing state to leak between calls.

## Architecture

- **`toolbox/`** — Python package with two modules:
  - `text_utils.py` — `is_palindrome()`, `word_frequency()` (not yet implemented)
  - `convert_utils.py` — `celsius_to_fahrenheit()`, `moving_average()`, `tag_reading()` (all stubs except `tag_reading`)
- **`tests/`** — pytest files mirror the module structure (`test_text_utils.py`, `test_convert_utils.py`)
