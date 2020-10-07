#!/usr/bin/python3
"""This module writes a class Student that defines a student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a
        Student instance"""
        if attrs is None or type(attrs) != list:
            return self.__dict__
        dic = {}
        for item in attrs:
            if type(item) != str:
                return self.__dict__
            elif item in self.__dict__.keys():
                dic.update({item: self.__dict__.get(item)})
        return dic

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for k in json.keys():
            if k in self.__dict__.keys():
                self.__dict__[k] = json[k]
        return self.__dict__
