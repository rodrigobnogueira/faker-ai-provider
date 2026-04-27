# Agent Guidance

This repository contains a Faker provider for generating AI and machine-learning
test data. Keep changes small, data-focused, and easy to verify.

## Project Conventions

- Use the existing provider API shape in `faker_ai/provider.py`.
- Keep model metadata in `faker_ai/model_correlations.py` as plain structured data.
- Prefer adding focused tests in `tests/test_provider.py` when changing catalog behavior.
- Run `python -m pytest` before opening a PR when dependencies are available.
- Do not include local environment files such as `.venv/`, `.pytest_cache/`, or editor files in commits.

## Model Catalog Updates

- Model catalog updates should be additive by default.
- Do not remove an existing model when adding newer models unless the user clearly asks for removal, or unless there is a verified reason such as a duplicate, typo, or demonstrably invalid/speculative entry.
- When replacing a model name with a more accurate current name, consider keeping the older verified model too if it is a real historical, legacy, deprecated, or superseded model.
- If a vendor does not publish parameter counts, use `undisclosed` instead of inventing a value.
- Prefer official vendor documentation, model cards, or release notes when checking model names and capabilities.
- Preserve useful historical coverage. This provider is for realistic fake data, so it may include current, legacy, deprecated, and open historical models.

## Publishing a Release

- Publish only from an up-to-date `main` branch after all intended PRs are merged.
- Check PyPI for the latest published `faker-ai-provider` version before choosing the next version.
- Update both `pyproject.toml` and `faker_ai/__init__.py` to the same release version.
- Run the test suite and build checks before uploading: `python -m pytest`, `python -m build`, and `python -m twine check dist/*`.
- Build fresh artifacts for the version being published. Do not upload stale files from an old `dist/` directory.
- Commit the version bump before publishing.
- Always create and push a matching git tag for every published version, using the format `vX.Y.Z`.
- Upload the checked wheel and source distribution to PyPI with Twine or the repository's configured trusted-publishing workflow.
- After publishing, verify the new version is visible on PyPI and that the git tag points at the release commit.
- Download the published package from PyPI into a fresh environment and run a smoke test against the installed package.
