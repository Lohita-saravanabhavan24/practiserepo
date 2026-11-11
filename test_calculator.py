import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

import calculator


class CalculatorOperationTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
# changes 
    def test_subtract(self):
        self.assertEqual(calculator.subtract(7, 4), 3)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.divide(8, 2), 4)

    def test_divide_by_zero_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            calculator.divide(1, 0)


class CalculatorCliTests(unittest.TestCase):
    @patch("builtins.input", side_effect=["1", "2", "3", "5"])
    def test_main_runs_operation_and_quits(self, _mock_input):
        output = StringIO()
        with redirect_stdout(output):
            calculator.main()

        self.assertIn("1. Add", output.getvalue())
        self.assertIn("Result: 5.0", output.getvalue())
        self.assertIn("Goodbye!", output.getvalue())

    @patch("builtins.input", side_effect=["invalid", "5"])
    def test_main_reports_invalid_menu_choice(self, _mock_input):
        output = StringIO()
        with redirect_stdout(output):
            calculator.main()

        self.assertIn("Invalid choice.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
