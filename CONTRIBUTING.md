# Contributing

Thanks for helping improve `faker-ai-provider`. This file is the human-facing summary of
the rules in [AGENTS.md](AGENTS.md); that file stays the source of truth for
agent-specific guidance and for the release checklist, so when the two disagree, follow
AGENTS.md and fix this file in the same change.

Changes here should stay small, data-focused, and easy to verify.

## Supported versions

- Python 3.10, 3.11, 3.12, 3.13, and 3.14 — the classifiers in `pyproject.toml` and the CI
  matrix must always list the same set.
- Faker 18.0.0 or newer (`faker>=18.0.0`). Do not use Faker APIs that are unavailable on
  that floor without raising the floor in `pyproject.toml`.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
pre-commit install
```

Never commit local environment artifacts — `.venv/`, `.pytest_cache/`, `dist/`, editor
files.

## Running the checks

CI runs exactly these four commands, and `.pre-commit-config.yaml` runs the same lint and
type-check arguments, so a clean local run is a clean CI run:

```bash
python -m pytest
python -m ruff check .
python -m ruff format --check .
python -m mypy --ignore-missing-imports --no-strict-optional .
```

`python -m ruff check . --fix` and `python -m ruff format .` apply the fixes. Run them from
the repository root: the linter covers `demo.ipynb` as well as the package sources, and the
formatter additionally reformats the Python blocks inside Markdown files, so README examples
are held to the same style.

## Seeded determinism

Reproducible output is the contract this provider sells, so:

- Every generator draws randomness from the provider's own RNG (`self.random_element`,
  `self.random_int`, and friends). Never use the `random` module directly, and never reach
  for wall-clock time, `uuid`, or process state — those break `seed_instance()`.
- The same seed and the same catalogue must produce the same values in the same order.
  `tests/test_provider.py::TestSeeding` guards this; keep it passing.
- Catalogue edits shift the seeded sequence by design: `ai_model()` picks over the catalogue
  keys and several helpers pick over sorted derived tuples, so adding, removing, or renaming
  an entry changes what seed 42 returns. That is expected — which is why tests assert
  relationships and membership rather than hard-coded seeded values. Do not add assertions
  that pin a specific model to a specific seed.
- Correlated helpers must stay internally consistent: `model_scenario()`,
  `ai_model_description()`, `full_ai_model_spec()`, `ai_training_run()`, and
  `ai_deployment()` all have to agree with `ai_company_for_model()` and friends for the same
  model.

## Model catalogue rules

The catalogue lives in `faker_ai/model_correlations.py` as plain structured data, typed by
`ModelData` in `faker_ai/types.py`. Keep it data — no logic in that module.

- Catalogue updates are additive by default. Do not remove an existing model when adding
  newer ones unless the change is clearly requested, or there is a verified reason such as a
  duplicate, a typo, or a demonstrably invalid or speculative entry.
- Preserve useful historical coverage. Current, legacy, deprecated, and open historical
  models all belong here. When you replace a model name with a more accurate current name,
  consider keeping the older verified entry too.
- Verify every fact against official vendor documentation, model cards, or release notes
  before adding it. Announced-but-unreleased or rumoured models do not go in.
- If a vendor does not publish a parameter count, use `undisclosed` rather than inventing a
  number.
- Real model, vendor, framework, and dataset names are the point of this provider and are
  used nominatively to describe real products. That licence does not extend to making things
  up: never attribute an invented model to a real vendor, never invent a version number, and
  never fabricate capabilities, modalities, or release years. Everything the provider
  synthesises around the catalogue — endpoints, experiment IDs, metrics, versions — is
  obviously fake data and must stay that way.

## Tests for new data

New or changed data needs tests in `tests/test_provider.py`:

- Membership: assert the new entries are present in `MODEL_CORRELATIONS`, in the style of
  `test_catalog_includes_july_2026_refresh_models`.
- Correlation: assert the entry's relationships, not just its existence — company round-trips
  through `ai_company_for_model()` / `ai_model_for_company()`, tasks come back from
  `ai_tasks_for_model()`, parameters from `ai_parameters_for_model()`.
- Regression: models that were deliberately left out because they are unverified belong in
  the disjointness check (`test_catalog_omits_unverified_future_models`) so they cannot creep
  back in.
- Removals: if an entry really has to go, say why in the PR description and keep the
  legacy-coverage test honest.

This provider has no locale-specific data; if that ever changes, every locale added needs the
same membership and correlation coverage as the default one.

## Data provenance and licensing

- Only vendor-published facts go into the catalogue: model name, vendor, architecture family,
  modalities, task list, parameter count, release year. Cite the source (model card, release
  note, docs page) in the PR description so a reviewer can check it.
- Do not bulk-import an external catalogue, dataset, benchmark list, or scraped leaderboard.
  Compiled databases carry their own licence, and this package ships under MIT.
- If a contribution is derived from an external source, that source's licence must permit
  redistribution under MIT, and the PR must name the source and its licence. Anything
  unclear, `NoDerivatives`, or share-alike stays out.

## Pull requests

- Keep formatting-only changes in their own commit, separate from substantive edits.
- Run the four checks above before opening the PR.
- Version bumps and releases follow the checklist in [AGENTS.md](AGENTS.md); releases are
  published by pushing a `vX.Y.Z` tag, and `pyproject.toml` and `faker_ai/__init__.py` must
  carry the same version.
