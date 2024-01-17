#!/usr/bin/python3
''' Rectangle model
'''

from models.base import Base


class Rectangle(Base):
    '''Class: Rectangle
        inherits base'''

    def __init__(self, width, height, x = 0, y = 0, id = None):
        '''method __init__ initializes a rectangle
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''get the width of a rectangle'''
        return self.__width
    
    @width.setter
    def width(self, value):
        '''set the width of the rectangle'''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''get the height of a rectangle'''
        return self.__height
    
    @height.setter
    def height(self, value):
        '''set the height of the rectangle'''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''x getter'''
        return self.__x
    
    @x.setter
    def x(self, value):
        '''set x'''
        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''y getter'''
        return self.__y
    
    @y.setter
    def y(self, value):
        '''set y'''
        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''functioin area'''
        return self.__height * self.__width
    
    def display(self):
        '''function display - prints the rectangle to stdio with #'''
        for height in range(self.__height):
            for width in range(self.__width):
                print('#', end='')
            print('')
    
    def __str__(self):
        '''overide __str__ function'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def display(self):
        '''function display. Print the rectangle using #'''
        if self.__width == 0 or self.__height == 0:
            print('')
            return
        [print("") for y in range(self.__y)]
        for h in range(self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print("#", end="") for w in range(self.__width)]
            print("")

    def update(self, *args, **kwargs):
        '''Update a Rectangle.
        
        Args:
            *args (ints): New attribute values.
                - 1st argument is the id attribute
                - 2nd argument is the width attribute
                - 3rd argument is the height attribute
                - 4th argument is the x attribute
                - 5th argument is the y attribute
        '''
        if args and len(args):
            for index, value in enumerate(args):
                if args[index] is not None:
                    if index == 0:
                        self.id = value
                    if index == 1:
                        self.width = value
                    if index == 2:
                        self.height = value
                    if index == 3:
                        self.x = value
                    if index == 4:
                        self.y = value
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''function: to_dictionary
            returns the dictionary representation of the Rectangle ob'''
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }