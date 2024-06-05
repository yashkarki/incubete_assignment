from django.test import TestCase
from calculator.calculator import add

class CalculatorTests(TestCase):
    def test_empty_string_returns_0(self):
        self.assertEqual(add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers_comma_delimited(self):
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers_comma_delimited(self):
        self.assertEqual(add("1,2,3"), 6)

    def test_new_lines_between_numbers(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_different_delimiters(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_negative_numbers_throw_exception(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed: -2")
