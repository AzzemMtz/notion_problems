import unittest
from algoritmo import Algoritmo


class Test_Algoritmo(unittest.TestCase):

    def test_validation_parenthees(self):
        self.assertTrue(Algoritmo.valid_parentheses("()"),"Sholud be true")
        self.assertFalse(Algoritmo.valid_parentheses(")(()))"),"Sholud be false")
        self.assertFalse(Algoritmo.valid_parentheses("("),"Sholud be false")
        self.assertTrue(Algoritmo.valid_parentheses("(())((()())())"),"Sholud be true")

    def test_format_duration(self):
        self.assertEqual(Algoritmo.format_duration(62),"1 minute and 2 seconds")
        self.assertEqual(Algoritmo.format_duration(3662),"1 hour, 1 minute and 2 seconds")
        self.assertEqual(Algoritmo.format_duration(0),"now")
        self.assertEqual(Algoritmo.format_duration(7200),"2 hours")

    def test_movie(self):
        self.assertEqual(Algoritmo.movie(500, 15, 0.9),43)
        self.assertEqual(Algoritmo.movie(100, 10, 0.95),24)