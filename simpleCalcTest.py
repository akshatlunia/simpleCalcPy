import unittest
import simpleCalc

class testCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(simpleCalc.addition(10, 3), 13)
        self.assertEqual(simpleCalc.addition(3.4, -10.2), 13.6)
        self.assertEqual(simpleCalc.addition(5, 0), 5)
    def test_subtraction(self):
        self.assertEqual(simpleCalc.subtraction(10, 3), 7)
        self.assertEqual(simpleCalc.subtraction(3.4, -10.2), 13.6)
        self.assertEqual(simpleCalc.subtraction(5, 0), 5)
    def test_multiplication(self):
        self.assertEqual(simpleCalc.multiplication(10, 3), 30)
        self.assertEqual(simpleCalc.multiplication(3.4, -10.2), -34.68)
        self.assertEqual(simpleCalc.multiplication(5, 0), 0)
    def test_addition(self):
        self.assertEqual(simpleCalc.division(10, 4), 2.5)
        self.assertEqual(simpleCalc.division(4, -10), -0.4)
        self.assertEqual(simpleCalc.division(5, 0), "undefined")

if __name__ == '__main__':
    unittest.main()

