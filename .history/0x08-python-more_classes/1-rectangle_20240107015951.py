#!/usr/bin/python3
"""
Python more classes.
"""
class Rectangle:
    """
    class Rectangle
    """
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width
    
    def width(self, value):
        if not isinstance(value, (int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def height(self):
        return self.__height
    
    def height(self, value):
        if not isinstance(value, (int)):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__class__.__height = value
