# Greedy Coin Change

**A Python algorithm project by [Abdurakhman Sagyngaliyev](https://github.com/abdurrr2011).**

[![Tests](https://github.com/abdurrr2011/coin-change-greedy/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/abdurrr2011/coin-change-greedy/actions/workflows/tests.yml)
![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Dependencies: none](https://img.shields.io/badge/dependencies-none-2ea44f)

Explore coin selection, integer division, and the limits of greedy algorithms
through a compact Python implementation. This repository preserves my original
algorithm and welcomes improvements to its examples, explanations, and tooling.

[Get started](#get-started) · [Understand the algorithm](#understand-the-algorithm) ·
[Contribute](#contribute) · [Report an issue](https://github.com/abdurrr2011/coin-change-greedy/issues/new/choose)

## Get started

Install Python 3.10 or newer. No third-party packages are needed.

```bash
git clone https://github.com/abdurrr2011/coin-change-greedy.git
cd coin-change-greedy
python exchange.py
```

Enter an integer amount, then a line of space-separated coin denominations:

```text
28
10 5 1
```

The program prints `6`:

| Denomination | Coins selected | Remaining amount |
| --- | ---: | ---: |
| 10 | 2 | 8 |
| 5 | 1 | 3 |
| 1 | 3 | 0 |

## Understand the algorithm

For each supplied denomination, the program uses integer division to count how
many coins fit, then subtracts their value from the remaining amount. Each coin
denomination has an unlimited supply.

The original implementation is kept in `exchange.py`. It creates a descending
copy called `revers_c`, but its loop reads the original list `c`. **Input order
therefore matters:** supply denominations largest first for greedy selection.

| Input amount | Denominations | Current output | Explanation |
| ---: | --- | ---: | --- |
| 28 | `10 5 1` | 6 | Exact change with descending denominations |
| 6 | `1 3 4` | 6 | The first denomination consumes the amount |
| 6 | `4 3 1` | 3 | Greedy picks `4 + 1 + 1`; `3 + 3` is better |
| 3 | `2` | 1 | A leftover amount is not reported |

The program assumes valid input: it does not validate negative values or empty
coin lists, and a zero denomination raises `ZeroDivisionError`. Importing the
module reads standard input. Greedy selection does not always find the minimum
number of coins for arbitrary denominations.

Sorting costs O(n log n) and creates an O(n) copy, even though the current loop
does not use that copy. The selection loop costs O(n), assuming constant-time
integer arithmetic.

## Project layout

```text
exchange.py                 Original algorithm and console input
README.md                   Usage, examples, and current behavior
CONTRIBUTING.md             Contribution workflow
ROADMAP.md                  Suggested improvements
tests/test_exchange.py      Tests of the original program
.github/                    CI workflow and contribution templates
```

Contribution guidance and tests are proposed in separate pull requests and
become available on `main` when those pull requests are merged.

## Verify behavior

Once the testing pull request is merged, run:

```bash
python -m unittest discover -s tests -v
```

Six subprocess tests cover normal input, input order, zero amounts, greedy
limitations, remainders, and division by zero. GitHub Actions checks Python
3.10–3.14. The workflow badge reflects the default branch after CI is merged.

## Contribute

Start with [CONTRIBUTING.md](CONTRIBUTING.md) and [ROADMAP.md](ROADMAP.md) once
the contributor guidance pull request is merged. Good starting points include
worked examples, clearer explanations, and tests documenting current behavior.

Keep `exchange.py` unchanged. Discuss any proposed algorithm change in an issue
before implementing it. Focus each pull request on one useful improvement and
include verification details.

## Author

Maintained by **Abdurakhman Sagyngaliyev** ·
[GitHub profile](https://github.com/abdurrr2011) ·
[Project issues](https://github.com/abdurrr2011/coin-change-greedy/issues)
