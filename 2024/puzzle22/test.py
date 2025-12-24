import unittest

from puzzle22 import read_data, mix, get_next_num, get_final_num, solve_p1, solve_p2

class TestMain(unittest.TestCase):

    def test_mix(self):
        self.assertEqual(37, mix(42, 15))
    
    def test_next_num(self):
        self.assertEqual(15887950, get_next_num(123))
    
    def test_final_num(self):
        num_iters = 2000
        self.assertEqual(8685429, get_final_num(1, num_iters))
    
    def test_solve_p1(self):
        self.assertEqual(37327623, solve_p1(read_data('puzzle22_example.txt')))
    
    def test_solve_p2(self):
        self.assertEqual(23, solve_p2([1, 2, 3, 2024]))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)