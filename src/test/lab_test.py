import unittest

from src.main.user import User
from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_filter_columns(self):
        """
        This test compares the result of the problem1 function to the hardcoded values below which ensures that
        only the firstname column is retrieved.
        """
        # arrange
        expected_result = [
            User(0, "Steve", None),
            User(0, "Alexa", None),
            User(0, "Steve", None),
            User(0, "Brandon", None),
            User(0, "Adam", None),
        ]

        # act
        actual_result = problem1()

        # assert
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()
