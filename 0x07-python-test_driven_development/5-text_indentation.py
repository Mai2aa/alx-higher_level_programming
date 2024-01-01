#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """a function that prints a text with two lines after . ? :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuation_marks:
            lines.append(current_line.strip())
            lines.append("")  # Add two empty lines after the punctuation mark
            current_line = ""

    if current_line:
        lines.append(current_line.strip())

    formatted_text = "\n".join(lines)
    print(formatted_text)
