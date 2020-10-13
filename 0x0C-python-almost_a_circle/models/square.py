#!/usr/bin/python3
"""Class Square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes data"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Getting size value"""
        return self.width

    @size.setter
    def size(self, value):
        """Setting width and height"""
        self.integer_validator("width", value)
        self.width = value
        self.height = value

    def __str__(self):
        """Method to be used when use print on Square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) > 0:
            for i in range(len(args)):
                if i > 3:
                    break
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs.get(key)
                elif key == "size":
                    self.width = kwargs.get(key)
                    self.height = kwargs.get(key)
                elif key == "x":
                    self.x = kwargs.get(key)
                elif key == "y":
                    self.y = kwargs.get(key)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        d = {}
        d["id"] = self.id
        d["size"] = self.size
        d["x"] = self.x
        d["y"] = self.y
        return d
