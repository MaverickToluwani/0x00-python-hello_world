class Square:
    """ A simple class to define a square"""
    def __init__(self, size=0):
        """
        Conditional Loop below to check if value enters is an
        integer and if size > 0
        
        Args:
            size(int): size of square,default value is 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            
            self.__size = size
