# Python Project Template

A [copier] template, containing my preferred initial project setup.

## Features

* A `src` directory, because you should.
* [uv] for Python and dependency management
* [hatchling] for builds
* [pytest] for tests
* [ruff] for linting & formatting
* [Sphinx] docs
* [interrogate] for pydoc coverage
* [Just] for task running
* Versioning using git tags.
* [pre-commit] for Git hooks

## To-Do

* [GitHub Actions] for CI
* Changelog management with [towncrier]
* License file
* GitHub PR template, etc.
* Code coverage

## Documentation

This project template provides my preferred Python layout.

### Versioning

[hatch-vcs] is used for versioning, picking up the version number from the most recent git tag.

There's an issue that in a development environment,
the version number is frozen at the version set when the package was installed as editable.
A slightly [hacky][hatch-vcs-footgun] approach has been used in `_version.py` to provide an accurate "live" version number in all cases.
If you don't like it, remove `_get_hatch_version()` from `_version.py` and "hatchling" and "hatch-vcs" from the "dev" group in `pyproject.toml`.

## Open Questions

* Should the CLI be optional?
  (Leaning towards *yes*.)

[copier]: https://copier.readthedocs.io/en/stable/reference/cli/
[GitHub Actions]: https://docs.github.com/en/actions
[hatch-vcs]: https://github.com/ofek/hatch-vcs
[hatch-vcs-footgun]: https://github.com/maresb/hatch-vcs-footgun-example
[hatchling]: https://pypi.org/project/hatchling/
[interrogate]: https://pypi.org/project/interrogate/
[Just]: https://just.systems/man/en/
[pre-commit]: https://pre-commit.com/
[pytest]: https://docs.pytest.org/en/stable/
[ruff]: https://docs.astral.sh/ruff/
[Sphinx]: https://www.sphinx-doc.org/en/master/index.html
[towncrier]: https://github.com/twisted/towncrier
[uv]: https://docs.astral.sh/uv/
