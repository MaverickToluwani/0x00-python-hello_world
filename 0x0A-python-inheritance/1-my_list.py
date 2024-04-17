#!/usr/bin/python3

"""
    modules inherites from the list class
"""

class MyList(list):
    """class inherits from the list class"""
    def print_sorted(self):
        """ Displays sorted list """
        print(sorted(self))
