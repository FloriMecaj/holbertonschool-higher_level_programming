#!/usr/bin/python3
""""class square that inherits from rectangle"""


from .rectangle import Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """super method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
