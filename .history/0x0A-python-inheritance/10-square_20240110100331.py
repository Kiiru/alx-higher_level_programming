#!/usr/bin/python3
"""
more class base
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ definition of a Rectangle """
    def __init__(self, size):
        self.__size = size
        Rectangle.integer_validator(self, 'size', self.__size)

    def area(self):
        return self.__size * self.__size