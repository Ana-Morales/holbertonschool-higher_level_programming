#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Unittest for Base"""

    def test_instance(self):
        """Testing is an instance"""
        r1 = Rectangle(1, 2)
        self.assertIsInstance(r1, Base)
        self.assertIsInstance(r1, Rectangle)

    def test_number_attr(self):
        """Testing number of argumnets"""
        with self.assertRaises(TypeError):
            r = Rectangle(1)
        with self.assertRaises(TypeError):
            r = Rectangle(1, 1, 1, 1, 1, 1)

    def test_valid_attr(self):
        """Testing valid type and value of each attribute"""
        with self.assertRaises(TypeError, msg="width must be an integer"):
            r = Rectangle("1", 1)
        with self.assertRaises(ValueError, msg="width must be >= 0"):
            r = Rectangle(-1, 1)
        with self.assertRaises(TypeError, msg="height must be an integer"):
            r = Rectangle(1, "1")
        with self.assertRaises(ValueError, msg="height must be >= 0"):
            r = Rectangle(1, -1)
        with self.assertRaises(TypeError, msg="x must be an integer"):
            r = Rectangle(1, 1, "1")
        with self.assertRaises(ValueError, msg="x must be > 0"):
            r = Rectangle(1, 1, -1)
        with self.assertRaises(TypeError, msg="y must be an integer"):
            r = Rectangle(1, 1, 1, "1")
        with self.assertRaises(ValueError, msg="y must be > 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_id_rec(self):
        """Testing correct id assigment"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1)
        r3 = Rectangle(1, 1)
        r4 = Rectangle(1, 1, 0, 0, 10)
        r5 = Rectangle(1, 1)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r4.id, 10)
        self.assertEqual(r5.id, 4)

    def test_area(self):
        """Testing area method"""
        r6 = Rectangle(3, 2)
        r7 = Rectangle(2, 10)
        r8 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r6.area(), 6)
        self.assertEqual(r7.area(), 20)
        self.assertEqual(r8.area(), 56)

    def test_display(self):
        """Testing display method"""
        r9 = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            r9.display()
            self.assertEqual(buf.getvalue(), expected)
        r10 = Rectangle(2, 2)
        expected = "##\n##\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            r10.display()
            self.assertEqual(buf.getvalue(), expected)

    def test_str(self):
        """Testinf str method"""
        r11 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            print(r11)
            self.assertEqual(buf.getvalue(), expected)

    def test_update(self):
        """Testing update method"""
        r12 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (89) 4/10 - 2/3\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            r12.update(89, 2, 3, 4)
            print(r12)
            self.assertEqual(buf.getvalue(), expected)
        r13 = Rectangle(10, 10, 10, 10)
        expected = "[Rectangle] (89) 1/3 - 4/2\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            r13.update(x=1, height=2, y=3, width=4, id=89)
            print(r13)
            self.assertEqual(buf.getvalue(), expected)

    def test_to_dictionary(self):
        """Testing to dictionary method"""
        r14 = Rectangle(1, 1)
        r15 = Rectangle(10, 2, 1, 9, 1)
        expected = "[Rectangle] (1) 1/9 - 10/2\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            r15_dict = r15.to_dictionary()
            r14.update(**r15_dict)
            print(r14)
            self.assertEqual(buf.getvalue(), expected)
if __name__ == '__main__':
    unittest.main()
