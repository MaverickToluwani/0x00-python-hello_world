#!/usr/bin/python3

""" module to check if the object is an instance 
    of a class that inherited
    (directly or indirectly) from the specified class.
"""

def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """

    obj_class = obj.__class__

    return issubclass(obj_class, a_class) and obj_class != a_class

