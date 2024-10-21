import unittest
import io
import sys

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b2.id - 1, b3.id - 2)

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

    def test_save_load_file(self):
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        loaded = Base.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].id, 1)
        self.assertEqual(loaded[1].id, 2)

    def test_save_to_file_empty(self):
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            self.assertEqual(f.read(), "[]")


class TestRectangle(unittest.TestCase):

    def setUp(self):
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
        expected_output = "    ####\n    ####\n    ####\n    ####\n    ####\n    ####\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        self.assertEqual(str(self.rect), "[Rectangle] (1) 2/3 - 4/6")

    def test_update_with_args(self):
        self.rect.update(10, 5, 1, 1, 1)
        self.assertEqual(self.rect.id, 10)
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 1)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 1)

    def test_update_with_kwargs(self):
        self.rect.update(width=10, height=5, x=1, y=1)
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 5)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 1)

    def test_to_dictionary(self):
        expected_dict = {'id': self.rect.id, 'width': 4, 'height': 6, 'x': 2, 'y': 3}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

    def test_property_setters(self):
        self.rect.width = 10
        self.assertEqual(self.rect.width, 10)
        self.rect.height = 8
        self.assertEqual(self.rect.height, 8)
        self.rect.x = 5
        self.assertEqual(self.rect.x, 5)
        self.rect.y = 4
        self.assertEqual(self.rect.y, 4)

        with self.assertRaises(TypeError):
            self.rect.width = "string"
        with self.assertRaises(ValueError):
            self.rect.width = -5

    def test_property_getters(self):
        self.assertEqual(self.rect.width, 4)
        self.assertEqual(self.rect.height, 6)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)


class TestSquare(unittest.TestCase):

    def setUp(self):
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

    def test_update_with_args(self):
        self.square.update(10, 6, 3, 4)
        self.assertEqual(self.square.id, 10)
        self.assertEqual(self.square.size, 6)
        self.assertEqual(self.square.x, 3)
        self.assertEqual(self.square.y, 4)

    def test_update_with_kwargs(self):
        self.square.update(size=8, x=2, y=3)
        self.assertEqual(self.square.size, 8)
        self.assertEqual(self.square.x, 2)
        self.assertEqual(self.square.y, 3)

    def test_to_dictionary(self):
        expected_dict = {'id': self.square.id, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(self.square.to_dictionary(), expected_dict)

    def test_property_setters(self):
        self.square.size = 10
        self.assertEqual(self.square.size, 10)

        with self.assertRaises(TypeError):
            self.square.size = "string"
        with self.assertRaises(ValueError):
            self.square.size = -5

    def test_property_getters(self):
        self.assertEqual(self.square.size, 5)
        self.assertEqual(self.square.x, 1)
        self.assertEqual(self.square.y, 2)


if __name__ == '__main__':
    unittest.main()
