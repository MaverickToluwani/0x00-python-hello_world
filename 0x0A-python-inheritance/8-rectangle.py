#!/usr/bin/python3

"""module defines the BaseGeometry class"""


class BaseGeometry:
    """defines the geometry of a shape"""

    def area(self):
        """Area of the shape"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if isinstance(value, int) is not True:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):

    """class that defines a rectangle"""
    def __init__(self, width, height):
        """Initializing attribute
            Args:
                width(int)
                height(int)
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

