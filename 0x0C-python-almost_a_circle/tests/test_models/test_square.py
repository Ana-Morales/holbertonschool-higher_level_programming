#!/usr/bin/python3
"""Unittest for Square"""
import unittest
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Unittest for Base"""

    def test_instance(self):
        """Testing is an instance"""
        s1 = Square(1)
        self.assertIsInstance(s1, Base)
        self.assertIsInstance(s1, Rectangle)
        self.assertIsInstance(s1, Square)

    def test_number_attr(self):
        """Testing number of argumnets"""
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(1, 1, 1, 1, 1)

    def test_valid_attr(self):
        """Testing valid type and value of each attribute"""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            s = Square("1")
        with self.assertRaises(ValueError, msg="width must be >= 0"):
            s = Square(-1)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            s = Square(1, "1")
        with self.assertRaises(ValueError, msg="x must be > 0"):
            s = Square(1, -1)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            s = Square(1, 1, "1")
        with self.assertRaises(ValueError, msg="y must be > 0"):
            s = Square(1, 1, -1)

    def test_id_rec(self):
        """Testing correct id assigment"""
        Base._Base__nb_objects = 0
        s1 = Square(1)
        s2 = Square(1)
        s3 = Square(1)
        s4 = Square(1, 0, 0, 10)
        s5 = Square(1)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)
        self.assertEqual(s4.id, 10)
        self.assertEqual(s5.id, 4)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_area(self):
        """Testing area method"""
        s6 = Square(3)
        s7 = Square(2)
        s8 = Square(8, 0, 0, 12)
        self.assertEqual(s6.area(), 9)
        self.assertEqual(s7.area(), 4)
        self.assertEqual(s8.area(), 64)

    def test_display(self):
        """Testing display method"""
        s9 = Square(2, 2, 2)
        expected = "\n\n  ##\n  ##\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s9.display()
            self.assertEqual(buf.getvalue(), expected)
        s10 = Square(2)
        expected = "##\n##\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s10.display()
            self.assertEqual(buf.getvalue(), expected)

    def test_str(self):
        """Testinf str method"""
        s11 = Square(4, 2, 1, 12)
        expected = "[Square] (12) 2/1 - 4\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(s11)
            self.assertEqual(buf.getvalue(), expected)

    def test_update(self):
        """Testing update method"""
        s12 = Square(10, 10, 10)
        expected = "[Square] (89) 10/10 - 10\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s12.update(89)
            print(s12)
            self.assertEqual(buf.getvalue(), expected)
        expected = "[Square] (89) 10/10 - 2\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s12.update(89, 2)
            print(s12)
            self.assertEqual(buf.getvalue(), expected)
        expected = "[Square] (89) 4/10 - 2\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s12.update(89, 2, 4)
            print(s12)
            self.assertEqual(buf.getvalue(), expected)
        expected = "[Square] (89) 4/5 - 2\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s12.update(89, 2, 4, 5)
            print(s12)
            self.assertEqual(buf.getvalue(), expected)

        Base._Base__nb_objects = 0
        s13 = Square(10, 10, 10)
        expected = "[Square] (1) 10/10 - 1\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s13.update(size=1)
            print(s13)
            self.assertEqual(buf.getvalue(), expected)
        expected = "[Square] (1) 1/10 - 1\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s13.update(x=1)
            print(s13)
            self.assertEqual(buf.getvalue(), expected)
        expected = "[Square] (89) 2/10 - 1\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s13.update(x=2, id=89)
            print(s13)
            self.assertEqual(buf.getvalue(), expected)
        expected = "[Square] (89) 1/4 - 3\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s13.update(x=1, size=3, y=4)
            print(s13)
            self.assertEqual(buf.getvalue(), expected)

    def test_to_dictionary(self):
        """Testing to dictionary method"""
        s14 = Square(1)
        s15 = Square(10, 1, 9, 1)
        expected = "[Square] (1) 1/9 - 10\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s15_dict = s15.to_dictionary()
            s14.update(**s15_dict)
            print(s14)
            self.assertEqual(buf.getvalue(), expected)
            self.assertTrue(type(s15_dict) is dict)

if __name__ == '__main__':
    unittest.main()
