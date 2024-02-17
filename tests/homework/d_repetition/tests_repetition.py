import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):

    def test_get_factorial_1(self):
        self.assertEqual(get_factorial(4), 24)

    def test_get_factorial_2(self):
        self.assertEqual(get_factorial(5), 120)

    def test_get_factorial_3(self):
        self.assertEqual(get_factorial(6), 720)

    def test_sum_odd_numbers_1(self):
        self.assertEqual(sum_odd_numbers(7), 16)

    def test_sum_odd_numbers_2(self):
        self.assertEqual(sum_odd_numbers(9), 25)

    def test_sum_odd_numbers_3(self):
        self.assertEqual(sum_odd_numbers(10), 25)