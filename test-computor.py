import unittest
import computor

class Testmyabs(unittest.TestCase):
    def test_myabs(self):
        self.assertEqual(computor.myabs(1), 1, "Should be 1")
        self.assertEqual(computor.myabs(0), 0, "Should be 0")
        self.assertEqual(computor.myabs(-1), 1, "Should be 1")
        self.assertEqual(computor.myabs(-106), 106, "Should be 106")
        self.assertEqual(computor.myabs(-1.23), 1.23, "Should be 1.23")
        self.assertEqual(computor.myabs(4.34), 4.34, "Should be 4.34")

class Testmysqrt(unittest.TestCase):
    

    
if __name__ == '__main__':
    unittest.main()