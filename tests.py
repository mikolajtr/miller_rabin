import unittest

from miller_rabin import exp_sqr, is_prime


class ExponentiationBySquaringTestCase(unittest.TestCase):

    def test_small_integer(self):
        self.assertEqual(6561, exp_sqr(9, 4))

    def test_big_integer(self):
        self.assertEqual(89905445128575064923962694332222250418176, exp_sqr(12456, 10))

    def test_big_binary(self):
        self.assertEqual(115792089237316195423570985008687907853269984665640564039457584007913129639936, exp_sqr(2, 256))


class PrimalityTestCase(unittest.TestCase):

    def test_one(self):
        self.assertFalse(is_prime(1))

    def test_small_integer(self):
        self.assertTrue(is_prime(5))

    def test_even_integer(self):
        self.assertFalse(is_prime(8))

    def test_composite_integer(self):
        self.assertFalse(is_prime(91))

    def test_big_composite_integer(self):
        self.assertFalse(is_prime(exp_sqr(12456, 10)))
