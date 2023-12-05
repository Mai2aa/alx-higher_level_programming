#!/usr/bin/python3
"""Only sub class of"""
def inherits_from(obj, a_class):
    """checks if the object is an instance of a class that 
    inheited (directly or indirectly) from the specified class
    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    else:
        return False