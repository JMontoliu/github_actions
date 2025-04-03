import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_suma(self):
        self.assertEqual(self.calc.suma(5, 3), 8)
        self.assertEqual(self.calc.suma(0, 0), 0)

    def test_resta(self):
        self.assertEqual(self.calc.resta(7, 3), 4)
        self.assertEqual(self.calc.resta(5, 5), 0)

    def test_multiplicacion(self):
        self.assertEqual(self.calc.multiplicacion(2, 3), 6)
        self.assertEqual(self.calc.multiplicacion(0, 10), 0)

    def test_division(self):
        self.assertEqual(self.calc.division(8, 2), 4)
        self.assertRaises(ZeroDivisionError, self.calc.division, 5, 0)

    def test_rango(self):
        self.assertRaises(ValueError, self.calc.suma, 11, 3)
        self.assertRaises(ValueError, self.calc.resta, -1, 2)

if __name__ == '__main__':
    unittest.main()