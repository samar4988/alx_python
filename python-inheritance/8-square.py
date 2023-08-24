#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class baseGeo(type):
    """The custom metaclass"""
    def __dir__(self):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__()
                if attribute != '__init_subclass__']


class BaseGeometry(metaclass=baseGeo):
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            return value

    def __dir__(self):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__()
                if attribute != '__init_subclass__']


class Rectangle(BaseGeometry):
    """rectangle class"""

    def __init__(self, width, height):
        """initializing width and height"""
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)

    def __str__(self):
        """str method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """rectangle area"""
        return self.__width * self.__height


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initializing square size"""
        self.__size = super().integer_validator("size", size)
        super().__init__(size, size)
