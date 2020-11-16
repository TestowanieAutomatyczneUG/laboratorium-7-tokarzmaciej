import unittest
from sample.RomanNumber import *
from parameterized import parameterized, parameterized_class


class RomanParameterizedPackage(unittest.TestCase):

    def setUp(self):
        self.tmp = Roman()

    @parameterized.expand([
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (9, "IX"),
        (27, "XXVII"),
        (48, "XLVIII"),
        (49, "XLIX"),
        (59, "LIX"),
        (93, "XCIII"),
        (141, "CXLI"),
        (163, "CLXIII"),
        (402, "CDII"),
        (575, "DLXXV"),
        (911, "CMXI"),
        (1024, "MXXIV"),
        (3000, "MMM"),
    ])
    def test_roman_number_parameterized(self, romanNumber, expected):
        self.assertEqual(self.tmp.roman(romanNumber), expected)

    @parameterized.expand([
        (False,"You take bad type"),
        ('II', "You take bad type"),
        (1.3, "You take bad type"),

    ])
    def test_roman_number_exception_parameterized(self, romanNumber,expected):
        self.assertRaisesRegex(Exception,expected,self.tmp.roman, romanNumber)


if __name__ == '__main__':
    unittest.main()
