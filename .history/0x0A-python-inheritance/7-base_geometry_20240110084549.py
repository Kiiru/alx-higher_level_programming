#!/usr/bin/python3
"""module BaseGeometry."""
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