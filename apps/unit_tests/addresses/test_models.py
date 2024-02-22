from unittest import TestCase


class Dollar:
    def __init__(self, amount: int):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier

    def amounty(self) -> int:
        return self.amount


class SimpleTestCase(TestCase):
    def test_dollar(self):
        five = Dollar(5)
        five.times(2)
        self.assertEqual(10, five.amounty())
