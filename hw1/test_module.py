import unittest


def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        self.assertRaises(TypeError, factorize, 'string')
        self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        self.assertRaises(ValueError, factorize, -2)

    def test_zero_and_one_cases(self):
        self.assertEqual(factorize(0), (0,))
        self.assertEqual(factorize(1), (1,))

    def test_simple_numbers(self):
        self.assertEqual(factorize(3), (3,))
        self.assertEqual(factorize(13), (13,))
        self.assertEqual(factorize(29), (29,))

    def test_two_simple_multipliers(self):
        self.assertEqual(factorize(6), (2, 3))
        self.assertEqual(factorize(26), (2, 13))

    def test_many_multipliers(self):
        self.assertEqual(factorize(1001), (7, 11, 13, 77, 91, 143))


if __name__ == '__main__':
    # print(factorize(1001))
    unittest.main(exit=False)
