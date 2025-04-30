import unittest
from solucion import sumar_ascii

class TestSumarASCII(unittest.TestCase):
    def test_suma_ascii(self):
        self.assertEqual(sumar_ascii("hola mundo"), 999)
        self.assertEqual(sumar_ascii("Python"), 636)
        self.assertEqual(sumar_ascii(""), 0)
        self.assertEqual(sumar_ascii("123"), 150)
        self.assertEqual(sumar_ascii("ABC"), 198)

if __name__ == '__main__':
    unittest.main()