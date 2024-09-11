#!/usr/bin/python3
# square simulation
""" A module that defines a square"""


class Square:
    """A class representing a square shape

    Attributes:
        __size (int): The size of the square
        __position (tuple): coordinates of the square

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance with the given size

        Agrs:
            size (int): The size of the square
            position (tuple): coordinates of the square
        """
        self.size = size
        self.position = position

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
            TypeError: If value is not an integer
            ValueError: If value is less than or equals to 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Gets the position of the square
        Returns:
            position (tuple): coordinates of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the coordinates of the square
        Raises:
            TypeError: if value is not a tuple of 2 positive integer
        """
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ Calculates the area of the square
        Returns:
            int: The area of the square
        """
        return (self.__size)**2

    def square_coordinates(self):
        square_img = ""

        if self.size == 0:
            return square_img

        for y_coor in range(self.__position[1]):
            square_img += "\n"
        for row in range(self.size):
            square_img += " "*self.__position[0]
            for col in range(self.size):
                square_img += "#"
            if row < (self.size - 1):
                square_img += "\n"
        return square_img

    def my_print(self):
        """ Displays a # square
        """
        print(self.square_coorinates())

    def __str__(self):
        return self.square_coordinates()
