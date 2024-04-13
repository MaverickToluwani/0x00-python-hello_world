#!/usr/bin/python3

"""A module that defines a square"""


class Square:
    """A class representing a square shape.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """Initializes a Square instance with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
