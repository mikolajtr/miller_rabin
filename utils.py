from operator import mul


def exp_sqr(x, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return mul(x, exp_sqr(x, n-1))
    a = exp_sqr(x, n/2)
    return pow(a, 2)
