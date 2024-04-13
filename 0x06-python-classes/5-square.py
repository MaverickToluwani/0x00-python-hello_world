#!/usr/bin/python3

""" A module that defines a square"""


class Square:
    """A class representing a square shape

    Attributes:
        _size (int): The size of the square
    """

    def __init__(self, size):
        """Initializes a square instance with the given size

        Agrs:
            size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ Gets the value of the size of square
        Returns:
            size (int): size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size of the square.
        Args:
            value (int): The new size of he square

        Raises:
            TypeError: If valu is not an integer
            ValueError: If value is less than or equals to 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("Size must be >= 0")
            self.__size = value

    def area(self):
        """ Calculates the area of the square
        Returns:
            int: The area of the square
        """
        return (self.__size)**2

    def my_print(self):
        """ Displays a square
        """
        if self.__size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end="")
            print()
