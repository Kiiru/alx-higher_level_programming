from base import Base
class Rectangle(Base):
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x = 0, y = 0, id = None):
        super().__init__(self, id)
        self.width = width
        self.height = height
        self.x = x