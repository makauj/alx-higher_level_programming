#!/usr/bin/python3
"""base class"""
import json
import os
import csv
import turtle


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
        if (type(list_dictionaries) != list or not
        all(type(idx) == dict for idx in list_dictionaries)):
            raise TypeError("list_dictionary must be a list of dictionaries")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """method that writes the JSON string representation to a file"""
        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None or not all(isinstance(objs, (Rectangle, Square)) for objs in list_objs):
                f.write("[]")
            else:
                dict_list = [objs.to_dictionary() for objs in list_objs]
                f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """method to return the list of the JSON string representation"""
        if json_string is None or json_string == '':
            return []
        if not isinstance(json_string, str):
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """method returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as my_file:
                list_dict = cls.from_json_string(my_file.read())
                return [cls.create(**dic) for dic in list_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """method to save instances to a csv file"""
        filename = f"{cls.__name__}.csv"
        if not list_objs:
            return

        fields = list_objs[0].to_dictionary().keys()
        rows = [obj.to_dictionary().values() for obj in list_objs]

        with open(filename, "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            csvwriter.writerows(rows)

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        filename = f"{cls.__name__}.csv"

        if not os.path.exists(filename):
            return []

        with open(filename, "r", newline="") as csvfile:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            else:
                fieldnames = ["id", "size", "x", "y"]
            list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
            instances = [cls.create(**{k: int(v) for k, v in d.items()})
                         for d in list_dicts]
            return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#00FFFF")
        turt.pensize(5)
        turt.shape("classic")

        # Draw rectangles
        turt.color("#000000")
        for rect in list_rectangles:
            turt.penup()
            turt.goto(rect.x, rect.y)
            turt.pendown()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)

        # Draw squares
        turt.color("#FF0000")
        for sq in list_squares:
            turt.penup()
            turt.goto(sq.x, sq.y)
            turt.pendown()
            for _ in range(4):  # Squares have four sides
                turt.forward(sq.size)
                turt.left(90)

        turtle.done()
