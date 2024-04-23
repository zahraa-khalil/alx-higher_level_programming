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

    def test_update(self):
        """Test updating attributes with args and kwargs."""
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(2, 3, 4, 5, 6)
        self.assertEqual((rect.id, rect.width, rect.height, rect.x, rect.y), (2, 3, 4, 5, 6))

        rect.update(height=7, width=8, x=9, y=10, id=11)
        self.assertEqual((rect.id, rect.width, rect.height, rect.x, rect.y), (11, 8, 7, 9, 10))
    
    def test_to_dictionary(self):
        """Test dictionary representation of Rectangle."""
        rect = Rectangle(10, 15, 5, 5, 1)
        rect_dict = rect.to_dictionary()
        self.assertDictEqual(rect_dict, {'id': 1, 'width': 10, 'height': 15, 'x': 5, 'y': 5})


