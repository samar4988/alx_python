#!/usr/bin/python3
"""Defines a class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class."""

    if isinstance(obj, a_class):
        return True
    return False
