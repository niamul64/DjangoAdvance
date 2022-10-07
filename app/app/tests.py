from django.test import TestCase
from app.calc import add


class CalcTests(TestCase):
    def test_add_numbers_pass(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

    def test_add_numbers_fail(self):
        """Test that two numbers are added together"""
        # self.assertEqual(add(3,8),10)                 # to make it fail
        # it will pass now
        self.assertEqual(add(3, 7), 10)
