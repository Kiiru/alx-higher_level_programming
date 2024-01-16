#!/usr/bin/python3
''' Rectangle model
'''

from models.base import Base


class Rectangle(Base):
    '''Class: Rectangle
        inherits base'''
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x = 0, y = 0, id = None):
        '''method __init__ initializes a rectangle'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get the width of a rectangle'''
        return self.__width
    
    @width.setter
    def width(self, value):
        if type(value) is not int:
