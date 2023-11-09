#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new  = a_dictionary + a_dictionary.get(key, value)
    return new