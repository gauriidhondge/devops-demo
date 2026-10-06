"""Unit tests for app.py - run by the Jenkins 'Test' stage."""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import add, greet  # noqa: E402


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_greet(self):
        self.assertIn("Jenkins", greet("Jenkins"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
