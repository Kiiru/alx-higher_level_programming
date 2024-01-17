#!/usr/bin/python3
''' Rectangle model
'''

from models.rectangle import Rectangle

class Square(Rectangle):
    '''Class: Square
        inherits Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''constructor'''
        super().__init__(size, size, x, y)

    def __str__(self):
        '''str'''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)