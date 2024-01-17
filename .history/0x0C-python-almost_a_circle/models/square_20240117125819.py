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

    def update(self, *args, **kwargs):
        '''Update a Rectangle.
        
        Args:
            *args (ints): New attribute values.
                - 1st argument is the id attribute
                - 2nd argument is the size attribute
                - 3rd argument is the x attribute
                - 4th argument is the y attribute
        '''
        if args and len(args):
            for index, value in enumerate(args):
                if args[index] is not None:
                    if index == 0:
                        self.id = value
                    if index == 1:
                        self.size = value
                    if index == 2:
                        self.x = value
                    if index == 3:
                        self.y = value
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''function: to_dictionary
            returns the dictionary representation of the Rectangle object'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }