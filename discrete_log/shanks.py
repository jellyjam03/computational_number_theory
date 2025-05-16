import random as rd
import math
from sympy import nextprime, ceiling


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

def binary_search(v, x):
    lo, hi = -1, len(v)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if v[mid][1] >= x:
            hi = mid
        else:
            lo = mid
    if hi == len(v):
        hi -= 1
    return v[hi]



def shanks(alpha, beta, p):
    # p, a prime
    # alpha, a primitive root of Zp
    # beta, a member of Zp
    m = int(ceiling(math.sqrt(p - 1)))
    inv = pow(alpha, -m, p)

    # baby steps
    L = [(j, pow(alpha, j, p)) for j in range(0, m)]
    L = sorted(L, key = lambda x: x[1])

    # giant steps
    for i in range(0, m):
        x = (beta * pow(inv, i, p)) % p
        # search for x in pr2(L)
        res = binary_search(L, x)
        if res[1] == x:
            # found x in L
            return i * m + res[0]

if __name__ == '__main__':
    p = nextprime((1 << 32))
    alpha = get_generator(p)
    beta = rd.randint(1, p)

    epsilon = shanks(alpha, beta, p)
    print(epsilon, beta, pow(alpha, epsilon, p))