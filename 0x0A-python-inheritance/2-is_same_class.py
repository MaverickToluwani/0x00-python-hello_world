#!/usr/bin/python3

""" module checks if an object is an exact
    instance of a class
"""


def is_same_class(obj: 'class', a_class: 'class') -> bool:
    """checks if an object is an exact instance of class"""
    return True if type(obj) == a_class else False
