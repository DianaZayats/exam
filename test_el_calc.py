import unittest
from program import calculate_energy_cost

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

if __name__ == "__main__":
    unittest.main()
