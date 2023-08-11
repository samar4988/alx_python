#!/usr/bin/python3
"""Implementation of Square class that inherit from Rectangle"""


from models.rectangle import Rectangle
"""Importing from Ractangle"""

class Square(Rectangle):
    """
    Represents a square.
    Attributes:
        id (int): The identifier of the square.
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The identifier of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The desired size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is under or equals 0.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return a string representation of the Square instance.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"