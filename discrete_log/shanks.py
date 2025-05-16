import random as rd
from sympy import nextprime
# use Shanks' algorithm to calculate log_alpha(beta) modulo p

def prime_factors(n):
    res = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            res.append(d)
        while n % d == 0:
            n //= d
        d += 1
    if n > 1:
        res.append(n)
    return res


def get_generator(p):
    # p prime
    # returns a generator element of the group Zp
    phi = p - 1
    fact = prime_factors(phi)
    for g in range(2, p):
        # is g a generator of Zp?
        # phi = p1^e1 * p2^e2 * ... * pk^ek
        # g is a generator if g^(phi(p) / pi) != 1, i = 1, ..k

        for factor in fact:
            if pow(g, phi // factor, p) == 1:
                break
        else:
            return g

    return None

def shanks(alpha, beta, p):
    # p, a prime
    # alpha, a primitive root of Zp
    # beta, a member of Zp

    return None

if __name__ == '__main__':
    # p = nextprime((1 << 32))
    # alpha = get_generator(p)
    # beta = rd.randint(1, p)
    #
    # epsilon = shanks(alpha, beta, p)
    # print(epsilon, pow(alpha, epsilon, p))
    print(get_generator(17))
    pass