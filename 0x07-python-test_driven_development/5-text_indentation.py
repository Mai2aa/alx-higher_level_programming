#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    new = ''
    result = ''
    for char in text:
        new += char
        if char in characters:
            result += new + "\n\n"
            new = ''
    if new:
        result += new
    print(result)