#!/usr/bin/python3



class Rectangle(BaseGeometry):
    """ Class: Rectangle """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height