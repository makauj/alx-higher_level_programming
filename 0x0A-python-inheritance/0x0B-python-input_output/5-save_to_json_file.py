#!/usr/bin/python3
"""write an Object to a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """write a JSON representation of an object to a text file"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
