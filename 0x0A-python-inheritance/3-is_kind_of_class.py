#!/usr/bin/python3
"""Same class or inherit from"""
def is_kind_of_class(obj, a_class):
    """checks if the object is an instance of or is  an instance of a class
    that inherited of a class from the specified class"""
    if issubclass(a_class, type(obj)) or isinstance(obj, a_class):
        return True
    else:
        return False