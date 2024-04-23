import unittest
from models.square import Square  # Adjust import path as necessary

class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

class TestSquare(unittest.TestCase):
    def test_initialization(self):
        """Test initialization with valid parameters."""
        square = Square(3, 1, 2, 4)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 4)

    def test_size_setter(self):
        """Test the size setter for valid and invalid values."""
        square = Square(4)
        square.size = 5
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        
        with self.assertRaises(TypeError):
            square.size = '10'
        
        with self.assertRaises(ValueError):
            square.size = -1

    def test_string_representation(self):
        """Test the string representation of the square."""
        square = Square(5, 0, 0, 10)
        self.assertEqual(str(square), "[Square] (10) 0/0 - 5")

    def test_area(self):
        """Test the area calculation inherited from Rectangle."""
        square = Square(7)
        self.assertEqual(square.area(), 49)
    
    def test_update(self):
        """Test updating attributes using args and kwargs."""
        square = Square(1, 1, 1, 1)
        square.update(2, 3, 4, 5)
        self.assertEqual((square.id, square.size, square.x, square.y), (2, 3, 4, 5))

        square.update(size=10, x=20, y=30, id=40)
        self.assertEqual((square.id, square.size, square.x, square.y), (40, 10, 20, 30))
    
    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        square = Square(10, 5, 5, 1)
        expected_dict = {'id': 1, 'size': 10, 'x': 5, 'y': 5}
        self.assertDictEqual(square.to_dictionary(), expected_dict)
    
    def test_str(self):
        """Test the string representation of the square."""
        square = Square(10, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (4) 2/3 - 10")




