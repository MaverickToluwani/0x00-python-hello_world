#!/usr/bin/python3
"""Magic class"""
import math


class MagicClass:
    """" Magic class setup"""
    def __init__(self, radius):
        """
            Args:
                radius (int or float): radius of a shape
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """area of shape"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """"circumference of shape"""
        return 2 * math.pi * self.__radius
