#!/usr/bin/python3
''' models/base.py
'''

import json
class Base:
    ''' first class Base
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' initialize Base  __init__
        '''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        '''function: to_json_string
            Args:
                '''
        if list_dictionaries is None or not list_dictionaries:
            return '[]'
        return json.dumps(list_dictionaries)