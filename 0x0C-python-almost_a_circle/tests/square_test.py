#!/usr/binpython3
import unittest
import io
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.square = Square(5, 1, 2)

    def test_initialization(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)
        self.assertEqual(self.square.id, 1)

    def test_area(self):
        self.assertEqual(self.square.area(), 25)

    def test_str(self):
        self.assertEqual(str(self.square), "[Square] (1) 1/2 - 5/5")

    def test_update(self):
        self.square.update(10, 6, 3, 4)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 6)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 4)

    def test_to_dictionary(self):
        expected_dict = {'id': self.square.id, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
