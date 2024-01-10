#!/usr/bin/python3

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Class: Rectangle """
    def __init__(self, width, height):
        """function: __init__
                Args:
                    width: width of a rectangle
                    height: height of a rectangle
        """
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator("width", width)
        BaseGeometry().integer_validator("height", height)

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
                    string representation of the rectangle
        """
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))