#!/usr/bin/python3
import unittest
import io
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0
        self.rect = Rectangle(4, 6, 2, 3)

    def test_initialization(self):
        self.assertEqual(self.rect.width, 4)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)
        self.assertEqual(self.rect.id, 1)

    def test_area(self):
        self.assertEqual(self.rect.area(), 24)

    def test_display(self):
        expected_output = "\n\n\n  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (1) 2/3 - 4/6")

    def test_update(self):
        self.rect.update(10, 5, 1, 1, 1)
        self.assertEqual(self.rect.id, 10)
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 1)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 1)

    def test_to_dictionary(self):
        expected_dict = {'id': self.rect.id, 'width': 4, 'height': 6, 'x': 2, 'y': 3}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
