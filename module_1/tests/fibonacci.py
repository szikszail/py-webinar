import unittest
from parameterized import parameterized
from module_1.fibonacci import fibonacci


class FibinachiTest(unittest.TestCase):
    def test_return_number(self):
        result = fibonacci(2)
        self.assertTrue(type(result) is int)

    def test_return_0_if_negative(self):
        self.assertEqual(fibonacci(-2), 0)

    @parameterized.expand([
        [0, 0], [1, 1], [2, 1], [3, 2],
        [4, 3], [5, 5], [6, 8], [7, 13],
        [8, 21], [9, 34], [10, 55], [11, 89],
        [12, 144], [13, 233], [14, 377]
    ])
    def test_return_right_item(self, n, fib):
        self.assertEqual(fibonacci(n), fib)
