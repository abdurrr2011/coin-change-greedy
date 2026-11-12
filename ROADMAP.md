# Contribution ideas

These are suggested tasks, not promises or existing GitHub issues. Check for
ongoing work before starting. All tasks below leave `exchange.py` unchanged.

- **First contribution: worked examples.** Add `examples/README.md` with three
  descending-denomination inputs, expected outputs, and manual coin counts.
- **First contribution: explain input order.** Add a walkthrough comparing
  amount 6 with `1 3 4` and `4 3 1`, verifying both outputs with the script.
- **First contribution: documentation review.** Check setup instructions from
  a fresh clone and correct any unclear steps.
- **Tests: document remaining behavior.** Add subprocess tests for duplicate
  denominations, an empty denomination line, and incomplete input. Assert the
  actual behavior without modifying the algorithm.
- **Learning guide: greedy versus optimal.** Write a short explanation using
  amount 6 with denominations `4 3 1`; show why two 3-value coins are better.
- **Tooling: improve documentation checks.** Propose a lightweight Markdown
  check in an issue, including dependency and maintenance costs.

Algorithm fixes, validation, and alternative solvers require a separate discussion
with the maintainer and are outside the current contribution scope.
