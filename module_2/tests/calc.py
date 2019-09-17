import unittest
from module_2.calc import Calc


class CalculatorTests(unittest.TestCase):
    def test_should_have_value(self):
        """ calc(3).v // 3 """
        c = Calc(3)
        self.assertEqual(c.v, 3)

    # Calc(3).add(5).v // 8
    # Calc(3).minus(2).v // 1
    # Calc(4).sqrt().v // 2
    # Calc(3).times(10).v // 30
    # Calc(10).divide(2).v // 5
    # Calc(10).modulo(5).v // 0
    # Calc(5).divide(0) // throw error
    # Calc(-3).sqrt() // throw error
    # Calc(3).add(4)
    #     .minus(3)
    #     .times(6).v // 24

    # TODO: write test cases to test calculator
