import unittest
from lab1 import calc

class TestCalc(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """    
    def test_var_1(self):
        result = calc(-1, '-', -1)
        self.assertEqual(result, 0)
    def test_var_2(self):
        result = calc(100, '*', 0.01)
        self.assertEqual(result, 1)
    def test_var_3(self):
        result = calc(4, '/', 0)
        self.assertEqual(result, "Zero division")
if __name__ == '__main__':
    unittest.main()