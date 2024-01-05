#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Say My Name function

    Args:
        first_name: first name
        last_name: last name

    Returns:
        nothing
    """
    if not isinstance(first_name, (str)) or not isinstance(last_name, (str)):
        raise TypeError('first_name must be a string or last_name must be a string')
    print('My name id {:s} {:s}'.format(first_name, se))