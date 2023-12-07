#!/usr/bin/python3
"""search and update """


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    text = ""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding='utf-8') as w:
        w.write(text)
