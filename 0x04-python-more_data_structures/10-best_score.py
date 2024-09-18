#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or not isinstance(a_dictionary, dict):
        return None

    biggest_key = max(a_dictionary, key=a_dictionary.get)
    return biggest_key