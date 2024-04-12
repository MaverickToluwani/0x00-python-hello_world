#!/usr/bin/python3
class Square:
    """ A class to describe a square
    
    Attributes:
        __size (int): size of square
    """
    def __init__(self, size):
        """
        Conditional Loop below to check if value enters is an
        integer and if size < 0
        
        Args:
            size(int): size of square,default value is 0
        
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0 """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("Size must be >= 0")
            self.__size = size
            
    def area(self):
        """Calculate the area of the square
        
        Returns:
            int: Area of the square
        """
        return (self.__size)**2
    
