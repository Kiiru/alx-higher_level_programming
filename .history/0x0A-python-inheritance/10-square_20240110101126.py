#!/usr/bin/python3
"""
more class base
"""

Rectangle = __import__('9-rectangle').Rectangle

"""
Square class
"""
class Square(Rectangle):
    """ definition of a Square """
    def __init__(self, size):
        """ constructor and size """
        Rectangle.integer_validator(self, 'size', self.__size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    # def area(self):
    #     """ function: area """
    #     return self.__size * self.__size