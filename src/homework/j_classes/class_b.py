#
import unittest
from class_a import Die

class TestDie(unittest.TestCase):
    def test_roll_values(self):
        die = Die()
        results = set()
        # We perform multiple rolls to see if it gives values within the expected range
        for _ in range(100):
            die.roll()
            roll_value = die.get_rolled_value()
            self.assertTrue(1 <= roll_value <= 6, "Roll value out of valid range (1-6)")
            results.add(roll_value)
        # Check if multiple distinct values are possible over multiple rolls
        self.assertTrue(len(results) > 1, "Die should roll multiple distinct values")

if __name__ == "__main__":
    unittest.main()
