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

    def width(self):
        return self.__class__.__width
    
    def width(self, value):
        if not isinstance(value, (int)):
            raise TypeError('width must be an integer')
        if value < 0:
            raise
