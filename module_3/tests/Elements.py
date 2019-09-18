import unittest
from module_3.Elements import Elements

class ElementsTest(unittest.TestCase):
    def test_exist(self):
        self.assertNotEqual(Elements, None)