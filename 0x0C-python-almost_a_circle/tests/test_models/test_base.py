#!/usr/bin/python3
"""
The Unittest for (base.py)
"""


import unittest
import pycodestyle
from models.base import Base


class TestBase(unittest.TestCase):
    """
    class to test all senarios in base module
    """
    def test_pep8_conformance_test_base(self):
        """
        Test case to confirm be PEP 8 validated
        """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/base.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (pycodestyle)."
            )

    def test_module_documentation(self):
        """
        Test the module documentation
        """
        module_doc = len(Base.__doc__)
        self.assertGreater(module_doc, 0)

    def test_class_documentation(self):
        """
        Test the class documentation
        """
        class_doc = len(Base.__doc__)
        self.assertGreater(class_doc, 0)

    def test_constructor_documentation(self):
        """Test the constructor documentation"""
        constructor_doc = len(Base.__init__.__doc__)
        self.assertGreater(constructor_doc, 0)

    def test_to_json_string_documentation(self):
        """Test the to_json_string documentation"""
        to_json_doc = len(Base.to_json_string.__doc__)
        self.assertGreater(to_json_doc, 0)

    def test_from_json_string_documentation(self):
        """Test the from_json_string documentation"""
        from_json_doc = len(Base.from_json_string.__doc__)
        self.assertGreater(from_json_doc, 0)

    def test_save_to_file_documentation(self):
        """Test the save_to_file documentation"""
        save_to_file_doc = len(Base.save_to_file.__doc__)
        self.assertGreater(save_to_file_doc, 0)

# ====================================================
    def test_init(self):
        """
        testing for initialization
        test1 for test with 'id' provided
        """
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_for_many_create(self):
        """
        Test for the assignment of different id values
        No id provided, should assign id = 1 else assign exact value
        """
        instance1 = Base()
        instance2 = Base(100)
        instance3 = Base()
        instance4 = Base(-5)
        instance5 = Base(7)

        self.assertEqual(instance1.id, 1)
        self.assertEqual(instance2.id, 100)
        self.assertEqual(instance3.id, 2)
        self.assertEqual(instance4.id, -5)
        self.assertEqual(instance5.id, 7)

    def test_for_many_arguments(self):
        """
        Test for TypeError when too many arguments are passed
        to the Base constructor
        """
        with self.assertRaises(TypeError):
            Base(1, 2, 3, 4, 5)

    def test_to_json_string(self):
        """
        function that test if the method _to_json_string returns JSON
        string representation of dictionary list
        TEST:
            Test when list_dictionaries is None
            Test when list_dictionaries is empty
            Test with non-empty list_dictionaries
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        list_dicts = [{'key1': 1, 'key2': 2}, {'key3': 3, 'key4': 4}]
        self.assertTrue(type(Base.to_json_string(list_dicts)), str)
        self.assertEqual(Base.to_json_string(
            list_dicts), '[{"key1": 1, "key2": 2}, {"key3": 3, "key4": 4}]')

    def test_from_json_string(self):
        """
        from_json_string() method, which is used to convert a JSON
        string representation of a list of dictionaries to an actual
        list of dictionaries
        """
        json_str = '[{"key1": 1, "key2": 2}, {"key3": 3, "key4": 4}]'
        self.assertTrue(isinstance(Base.from_json_string(json_str), list))
        self.assertTrue(all(isinstance(elt, dict)
                            for elt in Base.from_json_string(json_str)))
        self.assertEqual(Base.from_json_string(
            json_str), [{"key1": 1, "key2": 2}, {"key3": 3, "key4": 4}])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(None), [])


if __name__ == '__main__':
    unittest.main()
