#!/usr/bin/python3
"""
more class base
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ definition of a Square """
    def __init__(self, size):
        """ constructor and size """
        self.__size = size
        su
        Rectangle.integer_validator(self, 'size', self.__size)

    def area(self):
        """ function: area """
        return self.__size * self.__size