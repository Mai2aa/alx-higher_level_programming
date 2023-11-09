#!/usr/bin/python3
def best_score(a_dictionary):
    best = 0
    if a_dictionary is None:
        return
    for i in a_dictionary:
        if a_dictionary[i] > best:
            best = a_dictionary[i]
    return best