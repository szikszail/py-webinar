import unittest
from module_3.Layout import Layout

class LayoutTest(unittest.TestCase):
    def test_exist(self):
        self.assertNotEqual(Layout, None)