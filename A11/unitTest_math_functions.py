import unittest
from math_functions import power, divide

class TestMathFunctions(unittest.TestCase):
    
    # test power func
    def test_power(self):
        self.assertEqual(power(2, 2), 4)
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(4, 2), 16)
    
    def test_power_zero(self):
        self.assertEqual(power(2, 0), 1)
        self.assertEqual(power(0, 2), 0)
        
    def test_power_negative(self):
        self.assertEqual(power(2, -1), 0.5) 
        self.assertEqual(power(-2, 2), 4) 
        self.assertEqual(power(-2, -2), 0.25)
    
    # test divide func
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(21, 3), 7)
    
    def test_divide_zero(self):
        self.assertEqual(divide(4, 0), "Cannot divide by zero")
        self.assertEqual(divide(0, 2), 0)
    
    def test_divide_negative(self):
        self.assertEqual(divide(10, -2), -5)
        self.assertEqual(divide(-9, -3), 3)

if __name__ == "__main__":
    unittest.main()