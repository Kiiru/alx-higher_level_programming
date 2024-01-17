#!/usr/bin/python3
''' Square model
'''

from models.rectangle import Rectangle

class Square(Rectangle):
    '''Class: Square
        inherits Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''method __init__ initializes a square
        Args:
            size (int): The width of the new Square
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''string function'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
    
    @property
    def size(self):
        '''size getter property'''
        return self.width
    
    @size.setter
    def size(self, value):
        '''function: size setter
            Arguments:
                size: int'''
        self.width = value
        self.height = value

    