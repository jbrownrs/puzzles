import unittest

import ecm_puzzle_module


class TestEcmPuzzle(unittest.TestCase):

    def test_round_down_three_sig(self):
        actual = ecm_puzzle_module.round_sig(1.234567, 3)
        expected = 1.23
        self.assertEqual(actual, expected)

    def test_round_up_three_sig(self):
        actual = ecm_puzzle_module.round_sig(9.87654, 3)
        expected = 9.88
        self.assertEqual(actual, expected)

    def test_dip_the_bowl_correct_answer(self):
        actual = ecm_puzzle_module.dip_the_bowl(10, 3)
        print(actual)
        expected = 2.93
        self.assertEqual(actual, expected)

    def test_test(self):
        actual = 1
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
