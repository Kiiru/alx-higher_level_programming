#!/usr/bin/python3
"""This is an empty BaseGeometry class."""
class BaseGeometry:
    """function: inherits_from 
    Args:
        obj: object
        a_class: class to check obj against
    Returns:
        True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.
    """
    def area(self):
        raise Exception("area() is not implemented")