#!/usr/bin/python3
"""base class"""
import json
import os
import csv


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns JSON string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        if (type(list_dictionaries) is not list or \
            not all(type(i) == dict for i in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string representation to a file"""
        with open((cls.__name__ + ".json"), "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(Base.to_json_string(
                    [objs.to_dictionary() for objs in list_objs]))
                
    @staticmethod
    def from_json_string(json_string):
        """method to return the list of the JSON string representation"""
        if json_string is None:
            return "[]"
        if json_string is not None and json_string != '':
            if type(json_string) != str:
                raise TypeError("json_string must be a string")
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """methos returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """retuens a list of instances"""
        json_file = cls.__name__ + ".json"
        instances_list = []
        dicts = []

        if os.path(json_file):
            with open(json_file, "r") as f:
                json_file = f.read()
                dicts = cls.from_json_string(json_file)
                for dictionary in dicts:
                    instances_list.append(cls.create(**dictionary))
        return instances_list

    @classmethod
    def save_to_file_csv(cls, list_obj):
        """method to save instances to a csv file"""
        filename = cls.__name__ + ".csv"
        if not list_obj:
            return
        
        fields = list_obj[0].__dict__.keys()
        rows = [obj.__dict_.values() for obj in list_obj]

        with open(filename, "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)
