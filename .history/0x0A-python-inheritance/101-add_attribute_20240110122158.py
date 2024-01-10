#!/usr/bin/python3
""" more modules and functions """
def add_attribute(*args):
    """function: add_attribute
            Args: 
                *args
            Returns:
                nothing
            """
    if "main" in str(type(args[0])):
        setattr(args[0], args[1], args[2])
    else:
        raise TypeError("can't add new attribute")