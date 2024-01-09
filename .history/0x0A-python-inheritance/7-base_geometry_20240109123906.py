#!/usr/bin/python3
"""This is an empty BaseGeometry class."""
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
            raise TypeError('<name> must be an integer')
        