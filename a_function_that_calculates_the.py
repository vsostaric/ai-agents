
import math

def calculate_natural_logarithm(number):
    """
    This function calculates the natural logarithm of a given number.

    Description:
    The natural logarithm is the logarithm to the base e (Euler's number). It is denoted by ln(x) and is the inverse operation of exponentiation. This function takes a positive real number as input and returns its natural logarithm.

    Parameters:
        number (float): The input number for which the natural logarithm is to be calculated.

    Returns:
        float: The natural logarithm of the input number.

    Examples:
        >>> calculate_natural_logarithm(10)
        2.302585092994046
        >>> calculate_natural_logarithm(100)
        4.605170186017947

    Edge Cases:
        If the input number is not a positive real number, the function raises a ValueError.
            >>> calculate_natural_logarithm(-1)
            ValueError: Input number must be greater than zero.

    """
    # Check if the input number is valid
    if number <= 0:
        raise ValueError("Input number must be greater than zero.")

    # Calculate and return the natural logarithm of the input number
    return math.log(number)

# Example usage:
print(calculate_natural_logarithm(10))  # Output: 2.302585092994046


import math
import unittest

def calculate_natural_logarithm(number):
    """
    This function calculates the natural logarithm of a given number.

    Description:
    The natural logarithm is the logarithm to the base e (Euler's number). It is denoted by ln(x) and is the inverse operation of exponentiation. This function takes a positive real number as input and returns its natural logarithm.

    Parameters:
        number (float): The input number for which the natural logarithm is to be calculated.

    Returns:
        float: The natural logarithm of the input number.

    Examples:
        >>> calculate_natural_logarithm(10)
        2.302585092994046
        >>> calculate_natural_logarithm(100)
        4.605170186017947

    Edge Cases:
        If the input number is not a positive real number, the function raises a ValueError.
            >>> calculate_natural_logarithm(-1)
            ValueError: Input number must be greater than zero.

    """
    # Check if the input number is valid
    if number <= 0:
        raise ValueError("Input number must be greater than zero.")

    # Calculate and return the natural logarithm of the input number
    return math.log(number)

class TestCalculateNaturalLogarithm(unittest.TestCase):
    
    def test_basic_functionality(self):
        self.assertEqual(calculate_natural_logarithm(10), 2.302585092994046)
        self.assertEqual(calculate_natural_logarithm(100), 4.605170186017947)
        
    def test_edge_cases(self):
        with self.assertRaises(ValueError):
            calculate_natural_logarithm(-1)
        with self.assertRaises(ValueError):
            calculate_natural_logarithm(0)
        with self.assertRaises(ValueError):
            calculate_natural_logarithm(-10)
            
    def test_error_cases(self):
        self.assertEqual(calculate_natural_logarithm(math.nan), float('-inf'))
        self.assertEqual(calculate_natural_logarithm(float('inf')), float('inf'))
        
    def test_large_input(self):
        self.assertEqual(calculate_natural_logarithm(1000000), 13.815517)
        self.assertEqual(calculate_natural_logarithm(10**300), 301.459818)
        
    def test_small_input(self):
        self.assertEqual(calculate_natural_logarithm(1e-6), -4.605170186017947)
        self.assertEqual(calculate_natural_logarithm(5*10**-7), -5.298235)
        
if __name__ == '__main__':
    unittest.main()