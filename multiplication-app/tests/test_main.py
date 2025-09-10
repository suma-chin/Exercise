import unittest
from src.main import multiply_two_digits
from src.utils import validate_input

class TestMultiplication(unittest.TestCase):

    def test_multiply_valid_input(self):
        self.assertEqual(multiply_two_digits(12, 34), 408)
        self.assertEqual(multiply_two_digits(56, 78), 4368)

    def test_multiply_invalid_input(self):
        with self.assertRaises(ValueError):
            multiply_two_digits(12, 'a')
        with self.assertRaises(ValueError):
            multiply_two_digits('b', 34)

    def test_validate_input(self):
        self.assertTrue(validate_input(12))
        self.assertTrue(validate_input(99))
        self.assertFalse(validate_input(100))
        self.assertFalse(validate_input(-1))

if __name__ == '__main__':
    unittest.main()