#!/usr/bin/python3
''' Rectangle model
'''

from models.base import Base


class Rectangle(Base):
    '''Class: Rectangle
        inherits base'''

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
        '''set the width of the rectangle'''
        if type(value) is not int:
            raise TypeError('Width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''get the height of a rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''set the height of the rectangle'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x
    
    @x.setter
    def x(self, val):
        '''set x'''
        if type(val) is not int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be > 0')
        self.__x = val

    @property
    def y(self):
        '''y getter'''
        return self.__y
    
    @y.setter
    def y(self, val):
        '''set y'''
        if type(val) is not int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be > 0')
        self.__y = val