#!/usr/bin/python3
import unittest
import io
import sys
import os


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_initialization(self):
        b1 = Base()
        b2 = Base(42)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 42)



    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")
        with self.assertRaises(TypeError):
            Base.to_json_string("not a list")
        self.assertEqual(Base.to_json_string([{"id": 1}]), '[{"id": 1}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        with self.assertRaises(TypeError):
            Base.from_json_string(123)
        self.assertEqual(Base.from_json_string('[{"id": 1}]'), [{"id": 1}])

class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 105)

    def test_save_to_file_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_two_squares(self):
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 77)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(10, 7, 2, 8)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_overwrite(self):
        s = Square(9, 2, 39, 2)
        Square.save_to_file([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


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
