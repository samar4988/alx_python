#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class baseGeo(type):
    """The custom metaclass"""
    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

class BaseGeometry(metaclass = baseGeo):
    """Represent base_geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
    def __dir__(cls):
        """Overrides dir() method for the metaclass"""
        return [attribute for attribute in super().__dir__() if attribute !='__init_subclass__']
