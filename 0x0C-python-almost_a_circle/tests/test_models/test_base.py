#!/usr/bin/python3
"""Unittest for Base"""
import unittest
import json
import contextlib
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestBaseCls(unittest.TestCase):
    """Unittest for Base"""

    def test_id(self):
        """Testing correct id assigment"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

    def test_instante(self):
        """Testing is an instance of Base"""
        b6 = Base()
        self.assertTrue(isinstance(b6, Base))

    def test_attr_nb(self):
        """Testing nb_objects is a private instance attribute"""
        b7 = Base()
        with self.assertRaises(AttributeError):
            print(b7.nb_objects)
        with self.assertRaises(AttributeError):
            print(b7.__nb_objects)

    def test_to_json_string(self):
        """Testing to jason string method"""
        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dic = Base.to_json_string([d])
        self.assertTrue(type(json_dic) is str)

    def test_from_json_string(self):
        """Testing from json string method"""
        json_string = '[{"height": 4, "width": 10, "id": 89}]'
        ls = Base.from_json_string(json_string)
        self.assertTrue(type(ls) is list)

    def test_save_to_file(self):
        """Testing save to file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.dumps([r1.to_dictionary(),
                                         r2.to_dictionary()]), f.read())
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertEqual(json.dumps([s1.to_dictionary(),
                                         s2.to_dictionary()]), f.read())

    def test_create(self):
        """Testing create method"""
        r1 = Rectangle(3, 5, 1, 0, 1)
        r1_dictionary = r1.to_dictionary()
        expected = "[Rectangle] (1) 1/0 - 3/5\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            r2 = Rectangle.create(**r1_dictionary)
            print(r2)
            self.assertEqual(buf.getvalue(), expected)

        s1 = Square(3, 1, 0, 1)
        s1_dictionary = s1.to_dictionary()
        expected = "[Square] (1) 1/0 - 3\n"
        with StringIO() as buf, contextlib.redirect_stdout(buf):
            s2 = Square.create(**s1_dictionary)
            print(s2)
            self.assertEqual(buf.getvalue(), expected)

    def test_load_from_file(self):
        """Testing load from file method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(type(list_rectangles_output) is list)
        self.assertEqual(len(list_rectangles_output), 2)
        self.assertIsInstance(list_rectangles_output[0], Rectangle)
        self.assertEqual(list_rectangles_output[0].width, 10)

        Base._Base__nb_objects = 0
        s1 = Square(10, 2, 8)
        s2 = Square(2)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertTrue(type(list_squares_output) is list)
        self.assertEqual(len(list_squares_output), 2)
        self.assertIsInstance(list_squares_output[0], Square)
        self.assertEqual(list_squares_output[0].size, 10)

if __name__ == '__main__':
    unittest.main()
