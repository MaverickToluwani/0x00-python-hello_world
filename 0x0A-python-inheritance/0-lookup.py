#!/usr/bin/python3
"""
    This module returns the list of available attributes and methods
"""

def lookup(obj: 'class') -> list:
    """
    Returns the list of available
    attributes and methods of an object

    Returns:
        List: list of available obj attributes and methods
    """
    return dir(obj)
