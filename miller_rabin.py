from operator import mod, sub
from random import randint

from utils import exp_sqr


class PrimeComputingError(Exception):
    pass


def is_composite(a, n, d, s):
    x = mod(exp_sqr(a, d), n)
    if x != 1:
        prime = False
        for r in xrange(s):
            if exp_sqr(a, exp_sqr(2, r) * d) % n == n - 1:
                prime = True
        if not prime:
            return True
    return False


def is_prime(n, k=5):
    if n == 2:
        return True
    if n < 2 or n & 1 == 0:
        return False

    d = sub(n, 1)
    s = 0

    while d & 1 == 0:
        d /= 2
        s += 1

    for i in xrange(k):
        a = randint(2, n - 1)
        if is_composite(a, n, d, s):
            return False

    return True


def generate_prime(min_prime, max_prime, k=5):
    number = 1

    while not is_prime(number, k):
        number = randint(min_prime, max_prime)
    return number
