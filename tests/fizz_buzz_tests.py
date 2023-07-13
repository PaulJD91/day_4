import unittest
from src.fizz_buzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):
    def test_is_number_div_3_fizz(self):
        self.assertEqual("Fizz!", fizz_buzz(3))
    def test_is_number_div_5_buzz(self):
        self.assertEqual("Buzz!", fizz_buzz(5))
    def test_isnt_fizz_buzz(self):
        self.assertEqual("7", fizz_buzz(7))
    def test_is_fizz_buzz(self):
        self.assertEqual("FizzBuzz!", fizz_buzz(15))
    