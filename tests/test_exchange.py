"""Characterize the original program without changing or importing it."""

import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "exchange.py"


class ExchangeTests(unittest.TestCase):
    def run_script(self, text):
        return subprocess.run(
            [sys.executable, str(SCRIPT)], input=text, text=True,
            capture_output=True, check=False, timeout=5,
        )

    def test_descending_denominations(self):
        result = self.run_script("28\n10 5 1\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "6\n")

    def test_zero_amount(self):
        result = self.run_script("0\n10 5 1\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "0\n")

    def test_input_order_is_preserved(self):
        result = self.run_script("6\n1 3 4\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "6\n")

    def test_greedy_is_not_always_optimal(self):
        result = self.run_script("6\n4 3 1\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "3\n")

    def test_leftover_is_not_reported(self):
        result = self.run_script("3\n2\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "1\n")

    def test_zero_coin_raises(self):
        result = self.run_script("3\n0\n")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("ZeroDivisionError", result.stderr)


if __name__ == "__main__":
    unittest.main()
