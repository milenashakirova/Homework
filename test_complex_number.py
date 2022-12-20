import unittest

from complex_number import ComplexNumber


class TestSum(unittest.TestCase):

    def test_abs(self):
        """Test the abs function."""
        number = ComplexNumber(4, 3)
        abs_v = abs(number)
        self.assertEqual(abs_v, 5, "the abs value is wrong!")

    def test_sum(self):
        """Test the sum."""
        number1 = ComplexNumber(5, -6)
        number2 = ComplexNumber(-3, 2)
        result = number1 + number2
        self.assertEqual(result.get_real(), 2, "Should be 2!")
        self.assertEqual(result.get_imaginary(), -4, "Should be -4!")
        self.assertEqual(result, ComplexNumber(2, -4), "Should be 2 + -4i!")

    def test_mutiply(self):
        """Test the multiplication."""
        number1 = ComplexNumber(2, 3)
        number2 = ComplexNumber(-1, 1)
        result = number1 * number2
        self.assertEqual(result.get_real(), -5, "Should be -5!")
        self.assertEqual(result.get_imaginary(), -1, "Should be 10!")
        self.assertEqual(result, ComplexNumber(-5, -1), "Should be -5 + -1i!")

    def test_sub(self):
        """Test the subtraction."""
        number1 = ComplexNumber(5, -6)
        number2 = ComplexNumber(-3, 2)
        result = number1 - number2
        self.assertEqual(result.get_real(), 8, "Should be 8!")
        self.assertEqual(result.get_imaginary(), -8, "Should be -8!")
        self.assertEqual(result, ComplexNumber(8, -8), "Should be 8 + -8i!")

    def test_truediv(self):
        """Test the division."""
        number1 = ComplexNumber(-2, 1)
        number2 = ComplexNumber(1, -1)
        result = number1 / number2
        self.assertEqual(result.get_real(), -1.5, "Should be -1.5!")
        self.assertEqual(result.get_imaginary(), -0.5, "Should be -0.5!")
        self.assertEqual(result, ComplexNumber(-1.5, -0.5), "Should be -1.5 + -0.5i!")

    def test_str(self):
        """Test the print string."""
        number1 = ComplexNumber(-2, 1)
        self.assertEqual(number1.__str__(), "-2 + 1i", 'Should be "-2 + 1i"')


if __name__ == '__main__':
    unittest.main()