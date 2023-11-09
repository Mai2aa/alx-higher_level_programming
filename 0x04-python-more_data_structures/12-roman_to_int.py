#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return
    roman_value = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}
    prev = 0
    result = 0
    for i in roman_string[::-1]:
        value = roman_value.get(i, 0)
        if value >= prev:
            result += value
        else:
            result -= value
        prev = value
    return result
