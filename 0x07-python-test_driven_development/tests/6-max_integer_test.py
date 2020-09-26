#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer ([..])"""

    def test_max_at_beginning(self):
        """Test when the max int is at the beginnig of the list
        """
        ls = [10, 1, 2, 9, 5]
        self.assertEqual(max_integer(ls), 10)

    def test_max_at_end(self):
        """Test when the max int is at the end of the list
        """
        ls = [1, 2, 9, 5, 10]
        self.assertEqual(max_integer(ls), 10)

    def test_negative_numbers(self):
        """Test for a list with negative numbers
        """
        ls = [-10, -3, -1, -15]
        self.assertEqual(max_integer(ls), -1)

    def test_typeerror_1(self):
        """Test for a list with elements that are nor numbers
        """
        ls = [5, "4", 3, 2]
        with self.assertRaises(TypeError):
            max_integer(ls)

    def test_argument_notlist(self):
        """Test for an argument which is not a list
        """
        ls = "Hello"
        self.assertEqual(max_integer(ls), "o")

    def test_return_None(self):
        """Testing an empty list
        """
        ls = []
        self.assertEqual(max_integer(ls), None)

if __name__ == '__main__':
    unittest.main()
