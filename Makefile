
.PHONY: install test cli docs clean release verify

install:
	pip install -e .
	pip install torch matplotlib networkx sphinx

test:
	python -m unittest discover -s tests

cli:
	python cli.py --version
	python cli.py --train
	python cli.py --export --plot

docs:
	cd docs && sphinx-build -b html . _build/html

verify:
	python verify_env.py

release:
	version=$$(cat VERSION); \
	IFS='.' read -r major minor patch <<< "$$version"; \
	patch=$$((patch + 1)); \
	new_version="$$major.$$minor.$$patch"; \
	echo "$$new_version" > VERSION; \
	echo -e "\n## [$$new_version] - $$(date +'%Y-%m-%d')\n- Manual release via make" >> CHANGELOG.md; \
	git add VERSION CHANGELOG.md; \
	git commit -m "chore: bump version to $$new_version"; \
	git tag "v$$new_version"; \
	git push origin main --tags

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	rm -rf *.egg-info build dist .pytest_cache
