#!/usr/bin/python3
"""
test case for rectangle module
"""
import unittest
from models import rectangle
from models.base import Base
import pycodestyle
Rectangle = rectangle.Rectangle


class TestRectangle(unittest.TestCase):
    """
    unittest for Rectangle
    test for __str__, test converting a rectangle to a dictionary,
    Test initializing a rectangle with valid arguments,
    Test initializing a rectangle with invalid width
    """
    def setUp(self):
        Base._Base__nb_objects = 0
        pass

    def test_conformance(self):
        """
        Test that we conform to PEP-8
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/rectangle.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
        )

    def test_module_documentation(self):
        """Test the documentation of the module"""
        module_doc = __doc__
        self.assertIsNotNone(module_doc)
        self.assertNotEqual(len(module_doc), 0)

    def test_class_documentation(self):
        """Test the documentation of the Rectangle class"""
        class_doc = Rectangle.__doc__
        self.assertIsNotNone(class_doc)
        self.assertNotEqual(len(class_doc), 0)

    def test_area_documentation(self):
        """Test the documentation of the area method"""
        area_doc = Rectangle.area.__doc__
        self.assertIsNotNone(area_doc)
        self.assertNotEqual(len(area_doc), 0)

    def test_str_documentation(self):
        """Test the documentation of the __str__ method"""
        str_doc = Rectangle.__str__.__doc__
        self.assertIsNotNone(str_doc)
        self.assertNotEqual(len(str_doc), 0)

    def test_to_dictionary_documentation(self):
        """Test the documentation of the to_dictionary method"""
        to_dict_doc = Rectangle.to_dictionary.__doc__
        self.assertIsNotNone(to_dict_doc)
        self.assertNotEqual(len(to_dict_doc), 0)

    # testCase for __str__

    def test___str__(self):
        """Test the string representation of the rectangle"""
        r1 = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/3 - 5/10")

        r2 = Rectangle(3, 7, 0, 0, 2)
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 3/7")

        r3 = Rectangle(2, 2, 1, 1, 3)
        self.assertEqual(str(r3), "[Rectangle] (3) 1/1 - 2/2")

    # testCase for Area

    def test_area_calculation(self):
        """Test the calculation of the area"""
        r1 = Rectangle(5, 10)
        self.assertEqual(r1.area(), 50)

        r2 = Rectangle(3, 7)
        self.assertEqual(r2.area(), 21)

    # testCase for updating

    def test_update_with_kwargs(self):
        """kwargs"""
        r = Rectangle(5, 10, 2, 3, 1)
        r.update(width=7, height=8, x=9, y=1, id=2)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 2)

    # testCase for _to_dictionary

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 2, 3, 1)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), expected_dict)

        r = Rectangle(7, 12, 0, 0, 2)
        expected_dict = {'id': 2, 'width': 7, 'height': 12, 'x': 0, 'y': 0}
        self.assertEqual(r.to_dictionary(), expected_dict)

        r = Rectangle(10, 8, 4, 6, 4)
        expected_dict = {'id': 4, 'width': 10, 'height': 8, 'x': 4, 'y': 6}
        self.assertEqual(r.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
