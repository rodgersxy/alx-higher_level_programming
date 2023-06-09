#!/usr/bin/python3
"""Max integer - Unittest"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTestCase(unittest.TestCase):
    """
    class to test 6-max_integer_test.py with no
    arguments
    """

    def test_max_integer(self):
        """
        test case for list of integers with no
        arguments
        """
        test_max = [1, 2, 3, 4]
        self.assertEqual(max_integer(test_max), max(test_max))

    def test_max_mixed_numbers(self):
        """
        test case for list of +ve and -ve integers
        with no arguments
        """
        test_max = [-2, 5, -1, 10, 3, 12, -49]
        self.assertEqual(max_integer(test_max), max(test_max))

    def test_max_integer_floating(self):
        """
        test case floating list of integers with no
        arguments
        """
        test_max = [1.4, 2.4, 5.87, -4.7, -3.8]
        self.assertEqual(max_integer(test_max), max(test_max))

    def test_max_integer_one(self):
        """
        test case for one with no arguments
        """
        test_max = [9]
        self.assertEqual(max_integer(test_max), max(test_max))

    def test_max_integer_duplicates(self):
        """
        test case for duplicate numbers with no arguments
        """
        test_max = [10, 5, 10, 15, 3]
        self.assertEqual(max_integer(test_max), max(test_max))

    def test_max_integer_empty(self):
        """
        test case for empty list list ith no arguuments
        """
        test_max = []
        self.assertEqual(max_integer(test_max), None)

    def test_max_integer_large_numbers(self):
        """
        test case for large numbers
        """
        test_max = [1090000, 2100000, 3010000, 4000900]
        self.assertEqual(max_integer(test_max), max(test_max))

    def test_max_integer_two_elements(self):
        """
        Test case for a list with two elements
        """
        test_max = [3, 7]
        self.assertEqual(max_integer(test_max), max(test_max))
