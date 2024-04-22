import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

class TestRectangle(unittest.TestCase):
    def test_initialization(self):
        """Test initialization with valid parameters."""
        rect = Rectangle(3, 2, 1, 0, 10)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 0)
        self.assertEqual(rect.id, 10)

    def test_invalid_width(self):
        """Test initialization with invalid width."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_invalid_height(self):
        """Test initialization with invalid height."""
        with self.assertRaises(ValueError):
            Rectangle(1, 0)


    def test_area(self):
        """Test the area calculation."""
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)


    def test_update_args(self):
        """Test the update method with positional args."""
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 2, 2, 2, 2)
        self.assertEqual(rect.id, 2)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 2)

    def test_update_kwargs(self):
        """Test the update method with keyword args."""
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(height=10, width=10, x=10, y=10, id=10)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 10)
        self.assertEqual(rect.id, 10)
