import unittest
from module_3.Element import Element

class ElementTest(unittest.TestCase):
    def test_exist(self):
        self.assertNotEqual(Element, None)