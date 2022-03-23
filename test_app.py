import unittest
from app import Calc

class TestArea(unittest.TestCase):
    def setUp(self):
        self.calc = Calc()
    def test_add(self):
        self.assertEqual(self.calc.add(6,6), 12)