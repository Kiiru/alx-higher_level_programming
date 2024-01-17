#!/usr/bin/python3
''' Rectangle model
'''

from models.rectangle import Rectangle

class Square(Rectangle):
    '''Class: Square
        inherits Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, y, x)

    def __str__(self):
        