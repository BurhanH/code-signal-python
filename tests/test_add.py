import unittest
from ddt import ddt, data, unpack

from source import add 


@ddt
class TestAdd(unittest.TestCase):
    @data(
        (6, 5, 11),
        (0, 1000, 1000),
        (-2, 4, 2),
        (-100, 100, 0),
        (-100, 89, -11),
        (-1000, -999, -1999),
    )
    @unpack
    def test_add(self, param1, param2, result) -> None:
        self.assertEqual(add(param1, param2), result)
        
    @data(
        ('a', 5, 0),
        (None, None, 1000),
        (-2, 4, 2),
        (1001, 67, 0),
        (-5, -4352, 0)
    )
    @unpack
    def test_add(self, param1, param2, result) -> None:
        if param1 == None and param2 == None:
          self.assertEqual(add(), result)
        else:
          self.assertEqual(add(param1, param2), result)

if __name__ == '__main__':
    unittest.main()
