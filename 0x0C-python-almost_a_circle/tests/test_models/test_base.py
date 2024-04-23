#!/usr/bin/python3

import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """Test suite for the Base class."""

    def test_auto_id(self):
        """Test ID auto-increment functionality."""
        base1 = Base()
        base2 = Base()
        self.assertEqual(
            base1.id, 1, "Auto-incremented ID for base1 should be 1")
        self.assertEqual(
            base2.id, 2, "Auto-incremented ID for base2 should be 2")

    def test_explicit_id(self):
        """Test explicit ID assignment."""
        base3 = Base(10)
        self.assertEqual(base3.id, 10, "Explicit ID for base3 should be 10")

    def test_mixed_ids(self):
        """Test mixture of auto-assigned and explicit IDs."""
        base4 = Base()
        base5 = Base(20)
        base6 = Base()
        self.assertEqual(
            base4.id, 3, "Auto-incremented ID for base4 should be 3")
        self.assertEqual(base5.id, 20, "Explicit ID for base5 should be 20")
        self.assertEqual(
            base6.id, 4, "Auto-incremented ID for base6 should be 4 after an explicit ID assignment")


if __name__ == '__main__':
    unittest.main()
