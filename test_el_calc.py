import unittest
from unittest.mock import patch
from program import calculate_energy_cost, get_user_input

class TestCalculateEnergyCost(unittest.TestCase):

    def test_valid_input(self):
        self.assertAlmostEqual(calculate_energy_cost(100, 200, 0.5), 50.0)

    def test_negative_reading(self):
        with self.assertRaises(ValueError):
            calculate_energy_cost(-10, 200, 0.5)

    def test_end_less_than_start(self):
        with self.assertRaises(ValueError):
            calculate_energy_cost(200, 100, 0.5)

    def test_invalid_type(self):
        with self.assertRaises(ValueError):
            calculate_energy_cost("100", 200, 0.5)

class TestUserInput(unittest.TestCase):

    @patch('builtins.input', side_effect=['100', '200', '0.5'])
    def test_get_user_input_valid(self, mock_input):
        self.assertEqual(get_user_input(), (100, 200, 0.5))

    @patch('builtins.input', side_effect=['invalid', '200', '0.5'])
    def test_get_user_input_invalid_start(self, mock_input):
        self.assertIsNone(get_user_input())

    @patch('builtins.input', side_effect=['100', '-200', '0.5'])
    def test_get_user_input_negative_end(self, mock_input):
        self.assertIsNone(get_user_input())

if __name__ == "__main__":
    unittest.main()
