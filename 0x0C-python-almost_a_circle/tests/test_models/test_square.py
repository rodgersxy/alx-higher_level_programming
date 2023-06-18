#!/usr/bin/python3
"""
unittest - square.py module
"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    All test case scenario for class Square
    """

    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def test_correct_values(self):
        """
        Test correct values after updating attributes
        """
        square1 = Square(2, 4, 6)
        self.assertEqual(square1.size, 2)
        self.assertEqual(square1.x, 4)
        self.assertEqual(square1.y, 6)
        self.assertEqual(square1.id, 1)

        square2 = Square(2, 4, 6, 50)
        self.assertEqual(square2.size, 2)
        self.assertEqual(square2.x, 4)
        self.assertEqual(square2.y, 6)
        self.assertEqual(square2.id, 50)

        square3 = Square(2)
        self.assertEqual(square3.size, 2)
        self.assertEqual(square3.x, 0)
        self.assertEqual(square3.y, 0)
        self.assertEqual(square3.id, 2)

    def test_rectangle_is_subclass_of_base(self):
        """
        fuction that test if Rectangle is a subclass of Base
        """
        self.assertTrue(issubclass(Square, Base))

    def test_getters(self):
        """
        test for getters
        """
        square = Square(3, 4, 5, 6)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)
        self.assertEqual(square.id, 6)

    def test_setters(self):
        """
        test for setters and also
        Verify that the attributes have been updated correctly
        """
        square = Square(3, 4, 5, 6)
        square.size = 7
        square.x = 8
        square.y = 9
        square.id = 10

        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)
        self.assertEqual(square.id, 10)

    def test_float_size_type_error(self):
        """
        Attempt to create a square with float size
        This should raise a TypeError
        """
        with self.assertRaises(TypeError):
            Square(2.5)

    def test_float_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(2, 1.5)

    def test_float_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(2, 1, 2.5)

    def test_float_nan_size(self):
        with self.assertRaises(TypeError):
            Square(float('nan'), 10, 8)


if __name__ == '__main__':
    unittest.main()
