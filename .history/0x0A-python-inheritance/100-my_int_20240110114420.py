#!/usr/bin/python3
"""
more class base
"""

class MyInt(int):
    def __init__(self, num):
        self.num = num

    def __eq__(self, value):
        """ Invert the behavior of == """
        return self.num != value

    def __ne__(self, value):
        """ Invert the behavior of != """
        return self.num == value