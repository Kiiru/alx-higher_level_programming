#!/usr/bin/python3
"""module Rectangle"""
class Rectangle(BaseGeometry):
    __width = 0
    __height = 0
    def __init__(self, width, height):
        self