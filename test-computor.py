import unittest
import computor
import math
import re

class Testcomputor(unittest.TestCase):

    # mysqrt return the square root of a positif number
    def test_mysqrt(self):
        self.assertEqual(computor.mysqrt(0), math.sqrt(0), f"Should be ${math.sqrt(0)}")
        self.assertEqual(computor.mysqrt(1), math.sqrt(1), f"Should be {math.sqrt(1)}")
        self.assertEqual(computor.mysqrt(9), math.sqrt(9), f"Should be ${math.sqrt(9)}")
        self.assertEqual(computor.mysqrt(333), math.sqrt(333), f"Should be ${math.sqrt(333)}")

    # fraction() return the fraction form of a float
    def test_fraction_can_convert(self):
        self.assertEqual(computor.fraction(1.5), "3/2", "Should be 3/2")
        self.assertEqual(computor.fraction(2.5), "5/2", "Should be 5/2")
        self.assertEqual(computor.fraction(3.5), "7/2", "Should be 7/2")
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
    def test_myabs(self):
        self.assertEqual(computor.myabs(1), 1, "Should be 1")
        self.assertEqual(computor.myabs(0), 0, "Should be 0")
        self.assertEqual(computor.myabs(-1), 1, "Should be 1")
        self.assertEqual(computor.myabs(-106), 106, "Should be 106")
        self.assertEqual(computor.myabs(-1.23), 1.23, "Should be 1.23")
        self.assertEqual(computor.myabs(4.34), 4.34, "Should be 4.34")

    # swap the value between two variable
    def test_swap(self):
        self.assertEqual(computor.swap("1", "2"), ("2", "1"), "Should be swap")
        self.assertEqual(computor.swap(1, 2), (2, 1), "Should be swap")
        self.assertEqual(computor.swap(1, "2"), ("2", 1), "Should be swap")
        self.assertEqual(computor.swap("3 * x + 5", "2 * x^2"), ("2 * x^2", "3 * x + 5"), "Should be swap")

    def test_parsing_arg(self):
        self.assertEqual(computor.parsing_arg("4 * X^2 + 3 * X - 3 = 0"), [-3, 3, 4], "Should be [-3, 3, 4]")
        self.assertEqual(computor.parsing_arg("8 * X^2 + 2 * X = X + 4"), [-4, 1, 8], "Should be [-4, 1, 8]")
        self.assertEqual(computor.parsing_arg("8 * X^2 + 2 * X - 4 = + 2 * X - 4 + 8 * X^2"), [0, 0, 0], "Should be [0, 0, 0]")
        self.assertEqual(computor.parsing_arg("8 * X = + 2 * X - 4 + 8 * X^2"), [-4, -6, 8], "Should be [-4, -6, 8]")

    def test_parsing_arg_bad_input(self):
        with self.assertRaises(SystemExit):
            computor.parsing_arg("xx = 0")
        with self.assertRaises(SystemExit):
            computor.parsing_arg("4 **** X + 1 = X + 1")
        with self.assertRaises(SystemExit):
            computor.parsing_arg("1 * r 5 + 4 d = p 0")
        with self.assertRaises(SystemExit):
            computor.parsing_arg("543")
        with self.assertRaises(SystemExit):
            computor.parsing_arg("43,3 = x")
        with self.assertRaises(SystemExit):
            computor.parsing_arg("1/2 * X = 1")

    # list_equation take the reduced equation and return an array of coeff indexed by power
    def test_list_equation(self):
        self.assertEqual(computor.list_equation(re.split(r"(\+|-)", "2 * X + 1")), [1, 2], "Should be [1, 2]")
        self.assertEqual(computor.list_equation(re.split(r"(\+|-)", "X + 5 * X^3 + 4 * x^2")), [0, 1, 4, 5], "Should be [0, 1, 4, 5]")
        self.assertEqual(computor.list_equation(re.split(r"(\+|-)", "X^3")), [0, 0, 0, 1], "Should be [0, 0, 0, 1]")
        self.assertEqual(computor.list_equation(re.split(r"(\+|-)", "X + 3 * x - 2.2 * x^2")), [0 , 4, -2.2], "Should be [0, 4, -2.2]")

    # return the degree of the equation
    def test_get_degree(self):
        self.assertEqual(computor.get_degree([]), 0, "Should be 0")
        self.assertEqual(computor.get_degree([3, 4 , 2]), 2, "Should be 2")
        self.assertEqual(computor.get_degree([2]), 0, "Should be 0")
        self.assertEqual(computor.get_degree([2, 1]), 1, "Should be 1")
        self.assertEqual(computor.get_degree([2, 1, 4, 23]), 3, "Should be 3")
        self.assertEqual(computor.get_degree([2, 1, 4, 23, 3, 3, 2]), 6, "Should be 6")

    # return the delta of the equation
    def test_calc_delta(self):
        self.assertEqual(computor.calc_delta([4, 3, 2]), -23, "Should be -23")
        self.assertEqual(computor.calc_delta([-1, 32, 3]), 1036, "Should be 1036")
        self.assertEqual(computor.calc_delta([8, 3.4, 2]), -52.44, "Should be -52.44")
        self.assertEqual(computor.calc_delta([0, 2, 21]), 4, "Should be 4")
        self.assertEqual(computor.calc_delta([4, 0, 9]), -144, "Should be -144")
        self.assertEqual(computor.calc_delta([0, 0, 3]), 0, "Should be 0")

if __name__ == '__main__':
    unittest.main()
