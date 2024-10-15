#!/usr/bin/python3
"""function creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """open a JSON file and create an Object from its contents"""
    with open(filename, "r") as f:
        return json.loads(f)
