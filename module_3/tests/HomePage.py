import unittest
from module_3.HomePage import HomePage


class HomePageTest(unittest.TestCase):
    def test_exist(self):
        self.assertNotEqual(HomePage, None)
