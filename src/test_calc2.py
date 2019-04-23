#!/usr/bin/env python3.6

import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add_test1(self):
        self.assertEqual(calc.add(10, 5), 14)           # Fails 15 != 14
    
    def test_add_test2(self):
        self.assertEqual(calc.add(-1, 1), 0)
    
    def test_add_test3(self):
        self.assertEqual(calc.add(-1, -1), -3)          # Fails -2 != -3
        
    def test_subtract_test1(self):
        self.assertEqual(calc.subtract(10, 5), 2)       # Fails 5 != 2
        
    def test_subtract_test2(self):
        self.assertEqual(calc.subtract(-1, 1), -2)
        
    def test_subtract_test3(self):
        self.assertEqual(calc.subtract(-1, -1), -2)     # Fails 0 != -2
        
    def test_multiply_test1(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        
    def test_multiply_test2(self):
        self.assertEqual(calc.multiply(-1, 1), -1)
        
    def test_multiply_test3(self):
        self.assertEqual(calc.multiply(-1, -1), 1)     
    
    def test_divide_test1(self):
        self.assertEqual(calc.divide(10, 5), 2)
    
    def test_divide_test2(self):
        self.assertEqual(calc.divide(-1, 1), -1)
    
    def test_divide_test3(self):
        self.assertEqual(calc.divide(-1, -1), 1)

    def test_divide_zero_denominator_raises_exception(self):
        with self.assertRaisesRegex(ValueError, "Can not divide by zero!"):     # Message mismatch
            calc.divide(10, 0)
            
if __name__ == '__main__':
    unittest.main()
