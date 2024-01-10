#!/usr/bin/python3
"""
more class base
"""

class MyInt(int):
    
    def __eq__(self, other):
        """ Invert the behavior of == """
        return not super().__eq__(other)

    def __ne__(self, other):
        """ Invert the behavior of != """
        return not super().__ne__(other)