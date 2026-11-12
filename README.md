# Coin Change Algorithm

A small Python coin exchange project by Abdurakhman Sagyngaliyev.
The author's original algorithm is preserved in `exchange.py`.

## Run

Requires Python 3.10 or newer. No dependencies or installation needed.

```bash
python exchange.py
```

Enter the amount on the first line and space-separated coin denominations on
 the second line. For example:

```text
28
10 5 1
```

Output: `6`.

## How the current code behaves

The function processes denominations in their supplied order. Although it creates
`revers_c`, it currently reads `c` inside the loop. Supply denominations in
descending order to use largest-first selection. The code assumes valid input
and does not check for a leftover amount. Zero denominations cause division by
zero. Importing the module also reads standard input.

Greedy selection does not guarantee a minimum count for arbitrary denominations:
for amount 6 and coins `4 3 1`, it returns 3, while `3 + 3` uses 2 coins.

## Contribute

New contributors are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md),
which explains setup, scope, and how to submit a pull request. See
[ROADMAP.md](ROADMAP.md) for concrete contribution ideas.

The main algorithm is intentionally preserved. Please focus contributions on
examples, explanations, tests, and repository tooling. Propose algorithm changes
in an issue for the maintainer to consider before implementing them.

## Tests

```bash
python -m unittest discover -s tests -v
```

The tests execute the original script and document its existing behavior.
GitHub Actions runs them on Python 3.10–3.14.
