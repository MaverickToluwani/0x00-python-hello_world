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
