import unittest
from parameterized import parameterized
from module_1.euclidean import euclidean


class EuclideanTest(unittest.TestCase):
    def test_return_a_number(self):
        result = euclidean(1, 1)
        self.assertTrue(type(result) is int)

    def test_return_0_if_negative(self):
        self.assertEqual(euclidean(-2, 2), 0)

    def test_return_0_if_0(self):
        self.assertEqual(euclidean(0, 2), 0)

    @parameterized.expand([
        [1, 1, 1],
        [1, 7, 1],
        [128, 16, 16],
        [7, 9, 1],
        [6, 9, 3],
        [683, 997, 1]
    ])
    def test_return_right_GCD(self, a, b, result):
        self.assertEqual(euclidean(a, b), result)
