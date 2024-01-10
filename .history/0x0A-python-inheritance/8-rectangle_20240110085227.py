#!/usr/bin/python3
"""module Rectangle"""

class BaseGeometry:
    """ Class: BaseGeometry """
    def area(self):
        """function: area 
        Args:
            
        Returns:
            Exception
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        function: integer_validator
        Args:
            name: string
            value: int
        Returns:
            Nothing
        """
        if not isinstance(value, (int)):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
        

class Rectangle(BaseGeometry):
    __width = 0
    __height = 0
    def __init__(self, width, height):
        Rectangle.__width = witwidh
        Rectangle.__height = height