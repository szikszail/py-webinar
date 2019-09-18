import unittest
from module_4.arrayEqual import arrayEqual

class ArrayEqualTest(unittest.TestCase):
    def test_exist(self):
        self.assertNotEqual(arrayEqual, None)

    # TODO remaining tests