#!/usr/bin/python3


""" Checks if an object is an instance
    of or if object is and instance of
    a class that inherited from
"""


def is_kind_of_class(obj: 'class', a_class: 'class') -> bool:
    """checks if an object is an exact instance of class"""
    return isinstance(obj, a_class)
