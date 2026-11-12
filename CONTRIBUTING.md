# Contributing

Thanks for taking an interest in this project. Small, focused contributions
are welcome, including from people making their first pull request.

## Local setup

1. Fork this repository on GitHub and clone your fork.
2. Create a branch: `git switch -c docs/explain-example`.
3. Use Python 3.10 or newer; no third-party dependencies are required.
4. Run `python -m unittest discover -s tests -v`.

## Scope

Preserve `exchange.py`, the author's original main code. Useful contributions
include worked examples, documentation corrections, tests of current behavior,
and improvements to repository tooling. Discuss changes to the algorithm with
the maintainer in an issue before starting implementation.

Choose an idea from ROADMAP.md or open an issue describing your proposal. Check
existing issues and pull requests to avoid duplicate work. You do not need to
wait for assignment to submit a small documentation correction.

## Submit a pull request

Keep each pull request focused on one improvement. Explain the problem and the
result, link any related issue, and describe how you checked your work. For
examples, show the input and verify the output using the original script.

Run the tests before submitting. Do not commit credentials, generated caches,
or unrelated changes. Respond respectfully to review feedback. The maintainer
reviews contributions when available; there is no guaranteed review deadline.
