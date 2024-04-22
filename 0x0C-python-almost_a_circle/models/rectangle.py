#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class: inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x position of the rectangle
            y: y position of the rectangle
            id: id of object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def x(self):
        """getter the x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter the x coordinate"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """get the y value"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y value"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Display the rectangle"""
        print("\n" * self.y, end="")

        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                + f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """ Check the number of arguments and assign accordingly"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
    
