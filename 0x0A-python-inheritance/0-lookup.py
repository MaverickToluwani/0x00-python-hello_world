#!/usr/bin/python3
def lookup(obj: 'class') -> list:
    """
    Returns the list of available
    attributes and methods of an object

    Returns:
        List: list of available obj attributes and methods
    """
    return dir(obj)
