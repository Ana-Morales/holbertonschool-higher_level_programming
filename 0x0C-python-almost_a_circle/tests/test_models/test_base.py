#!/usr/bin/python3
"""Unittest for Base"""
import unittest
from models.base import Base


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

if __name__ == '__main__':
    unittest.main()
