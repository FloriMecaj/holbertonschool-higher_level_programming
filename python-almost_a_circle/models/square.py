#!/usr/bin/python3
""""class square that inherits from rectangle"""


from .rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """super method"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """__str__"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """update method"""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)
