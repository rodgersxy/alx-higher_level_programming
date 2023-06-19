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

    def test_boolean_size_type_error(self):
        """
        square with a boolean
        """
        with self.assertRaises(TypeError):
            Square(True, 9, 1)

    def test_boolean_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(2, True)

    def test_boolean_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(2, 1, True)

    def test_none_size_type_error(self):
        """
        square with None
        """
        with self.assertRaises(TypeError):
            Square(None)

    def test_none_x_type_error(self):
        with self.assertRaises(TypeError):
            Square(9, None)

    def test_none_y_type_error(self):
        with self.assertRaises(TypeError):
            Square(2, 9, None)

    # test case for __str__

    def test_str_representation(self):
        """
        square and check its string representation
        """
        square = Square(2, 3, 4, 5)
        expected_str = "[Square] (5) 3/4 - 2"
        self.assertEqual(str(square), expected_str)

    # test case for to_dictionary

    def test_to_dictionary(self):
        """
        to a dictionary
        """
        square = Square(2, 3, 4, 5)
        expected_dict = {'id': 5, 'size': 2, 'x': 3, 'y': 4}
        self.assertEqual(square.to_dictionary(), expected_dict)

    # test case for _update *args and **kwargs

    def test_update(self):
        """
        update using args then with kwargs
        """
        square = Square(2, 3, 4, 5)
        # square using *args
        square.update(6, 7, 8, 9)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

        # **kwargs
        square.update(id=10, size=11, x=12, y=13)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 11)
        self.assertEqual(square.x, 12)
        self.assertEqual(square.y, 13)

    # test case Area

    def test_area(self):
        """
        Calculate the area
        """
        square = Square(5)
        area = square.area()

        self.assertEqual(area, 25)


if __name__ == '__main__':
    unittest.main()
