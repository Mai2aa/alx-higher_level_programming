#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
    def test_middle(self):
        self.assertEqual(max_integer([1, 2, 9, 3, 4]), 9)
    def test_one_negative(self):
        self.assertEqual(max_integer([1, -2, 3, 9]), 9)
    def test_negatives(self):
        self.assertEqual(max_integer([-1, -2, -4, -6]), -1)
    def test_one_element(self):
        self.assertEqual(max_integer([4]), 4)
    def test_none(self):
        self.assertEqual(max_integer([]), None)
if __name__ == "__main__":
    unittest.main()