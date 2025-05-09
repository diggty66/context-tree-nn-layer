# Contributing to Context Tree NN Layer

Welcome! 👋

We follow clean, modular design practices (Skoda-style). To contribute:

## Development

1. Fork this repo
2. Clone locally and activate a Python 3.9 virtualenv
3. Run:
   ```
   make verify
   make install
   ```

## Code Style

- Follow Python PEP8 (use `flake8`)
- Keep modules minimal: 1 responsibility per file
- Docstrings in [Google/Napoleon format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- Use `make release` to bump version and update changelog

## Testing

- Add unit tests to `tests/`
- Run: `make test`

## Pull Requests

- Include clear descriptions
- Use conventional commit prefixes: `feat:`, `fix:`, `chore:`, etc.
- Target the `main` branch

Thanks for helping improve this project!
