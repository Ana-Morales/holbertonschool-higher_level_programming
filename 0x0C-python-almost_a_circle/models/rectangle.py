#!/usr/bin/python3
"""Class Rectangle"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes data"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getting width value"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setting width value"""
        self.integer_validator("width", width)
        self.__width = width

    @property
    def height(self):
        """Getting height value"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setting height value"""
        self.integer_validator("height", height)
        self.__height = height

    @property
    def x(self):
        """Getting x value"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setting x value"""
        self.integer_validator("x", x)
        self.__x = x

    @property
    def y(self):
        """Getting y value"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setting y value"""
        self.integer_validator("y", y)
        self.__y = y

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        elif (name == "x" or name == "y") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Returns the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print("\n" * self.__y, end="")
        print(((" " * self.__x) + ("#" * self.__width) + "\n")*self.__height,
              end="")

    def __str__(self):
        """Method to be used when use print on Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) > 0:
            for i in range(len(args)):
                if i > 4:
                    break
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        else:
            for key in kwargs.keys():
                if key == "id":
                    self.id = kwargs.get(key)
                elif key == "width":
                    self.__width = kwargs.get(key)
                elif key == "height":
                    self.__height = kwargs.get(key)
                elif key == "x":
                    self.__x = kwargs.get(key)
                elif key == "y":
                    self.__y = kwargs.get(key)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
