#!/usr/bin/python3

"""module defines the BaseGeometry class"""


class BaseGeometry:
    """defines the geometry of a shape"""

    def area(self):
        """Area of the shape"""
        raise Exception("area() is not implemented")
