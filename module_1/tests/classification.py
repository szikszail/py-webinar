import unittest
from parameterized import parameterized
from module_1.classification import grade


class GradeTest(unittest.TestCase):
    def test_return_a_number(self):
        result = grade(0)
        self.assertTrue(type(result) is int)

    def test_return_0_if_negative(self):
        self.assertEqual(grade(-1), 0)

    def test_return_0_if_score_is_bigger_than_maximum(self):
        self.assertEqual(grade(200), 0)

    @parameterized.expand([
        [0, 1], [20, 1], [59, 1],
        [60, 2], [61, 2], [69, 2],
        [70, 3], [71, 3], [79, 3],
        [80, 4], [81, 4], [89, 4],
        [90, 5], [91, 5], [100, 5]
    ])
    def test_return_right_grade(self, score, result):
        self.assertEqual(grade(score), result)


if __name__ == "__main__":
    unittest.main()
