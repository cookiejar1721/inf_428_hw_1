import unittest

from task import hours_difference

class TestHoursDifference(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(hours_difference(1, 5), 4)
        self.assertEqual(hours_difference(10, 15), 5)

    def test_crossing_day(self):
        self.assertEqual(hours_difference(23, 1), 2)
        self.assertEqual(hours_difference(1, 23), 22)

    def test_same_hour(self):
        self.assertEqual(hours_difference(12, 12), 0)
        self.assertEqual(hours_difference(0, 0), 0)

    def test_full_day(self):
        self.assertEqual(hours_difference(0, 24), 0)

if __name__ == "__main__":
    unittest.main()
