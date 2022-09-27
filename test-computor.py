import unittest
import computor
import math

# mysqrt return the square root of a positif number
class Testmysqrt(unittest.TestCase):
   def test_mysqrt(self):
        self.assertEqual(computor.mysqrt(0), math.sqrt(0), f"Should be ${math.sqrt(0)}")
        self.assertEqual(computor.mysqrt(1), math.sqrt(1), f"Should be {math.sqrt(1)}")
        self.assertEqual(computor.mysqrt(9), math.sqrt(9), f"Should be ${math.sqrt(9)}")
        self.assertEqual(computor.mysqrt(333), math.sqrt(333), f"Should be ${math.sqrt(333)}")

# fraction() return the fraction form of a float
class test_fraction(unittest.TestCase):
    def test_fraction_can_convert(self):
        self.assertEqual(computor.fraction(1.5), "3/2", "Should be 3/2")
        self.assertEqual(computor.fraction(2.5), "5/2", "Should be 5/2")
        self.assertEqual(computor.fraction(-3.43), "-343/100", "Should be -343/100")
        self.assertEqual(computor.fraction(-1.12), "-28/25", "Should be -28/25")
        self.assertEqual(computor.fraction(-13.65), "-273/20", "Should be -273/20")
        self.assertEqual(computor.fraction(45.12), "1128/25", "Should be 1128/25")
        self.assertEqual(computor.fraction(100.10000), "1001/10", "Should be 1001/10")

    def test_fraction_cant_convert(self):
        self.assertEqual(computor.fraction(234.987), "234.987", "Should be 234.987")
        self.assertEqual(computor.fraction(12345.1234), "12345.1234", "Should be 12345.1234")
        self.assertEqual(computor.fraction(985.1234), "985.1234", "Should be 985.1234")
        self.assertEqual(computor.fraction(1.074772708486752), "1.074772708486752", "Should be 1.074772708486752")

# myabs return the absolute value of a number
class Testmyabs(unittest.TestCase):
    def test_myabs(self):
        self.assertEqual(computor.myabs(1), 1, "Should be 1")
        self.assertEqual(computor.myabs(0), 0, "Should be 0")
        self.assertEqual(computor.myabs(-1), 1, "Should be 1")
        self.assertEqual(computor.myabs(-106), 106, "Should be 106")
        self.assertEqual(computor.myabs(-1.23), 1.23, "Should be 1.23")
        self.assertEqual(computor.myabs(4.34), 4.34, "Should be 4.34")

if __name__ == '__main__':
    unittest.main()
