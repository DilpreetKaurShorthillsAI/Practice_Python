import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add_both_positive(self):                                                                                            
        self.assertEqual(calc.add(10,5),15)

    def test_add_both_negative(self):                                                                                            
        self.assertEqual(calc.add(-10,-5),-15)

    def test_add_positive_negative(self):                                                                                            
        self.assertEqual(calc.add(10,-5),5)

    def test_add_zero(self):                                                                                            
        self.assertEqual(calc.add(10,0),10)

    def test_add_strings(self):                                                                                            
        self.assertEqual(calc.add("a","b"),"ab") 

    def test_subtract_both_positive(self):                                                                                            
        self.assertEqual(calc.subtract(10,5),5)

    def test_subtract_both_negative(self):                                                                                            
        self.assertEqual(calc.subtract(-10,-5),-5)

    def test_subtract_positive_negative(self):                                                                                            
        self.assertEqual(calc.subtract(10,-5),15)

    def test_substract_zero(self):                                                                                            
        self.assertEqual(calc.subtract(10,0),10)    

    def test_multiply_both_positive(self):                                                                                            
        self.assertEqual(calc.multiply(10,5),50)

    def test_multiply_both_negative(self):                                                                                            
        self.assertEqual(calc.multiply(-10,-5),50)

    def test_multiply_positive_negative(self):                                                                                            
        self.assertEqual(calc.multiply(10,-5),-50)

    def test_multiply_zero(self):                                                                                            
        self.assertEqual(calc.multiply(10,0),0)    

    def test_divide_both_positive(self):                                                                                            
        self.assertEqual(calc.divide(10,5),2)

    def test_subtract_both_negative(self):                                                                                            
        self.assertEqual(calc.divide(-10,-5),2)

    def test_subtract_positive_negative(self):                                                                                            
        self.assertEqual(calc.divide(10,-5),-2) 

    def test_divide(self):
        self.assertEqual(calc.divide(10, 2), 5) 
 
        with self.assertRaises(ZeroDivisionError) as context:
            calc.divide(5, 0)
 
        self.assertEqual(str(context.exception), "Can not divide by zero!")

if __name__ == '__main__':
    unittest.main()
