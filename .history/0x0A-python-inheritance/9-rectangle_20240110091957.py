#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Class: Rectangle """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """function: area
                Args:

                Returns:
                r   eturns the area of a rectangle
        """
        return self.__height * self.__width
    
    def __str__(self):
        """function: __str__
                Args:

                Returns:
        """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))