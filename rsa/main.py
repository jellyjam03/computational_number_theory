from sympy import nextprime
import random as rd
import time

# receive a list of tuples (b, m)
# meaning x congr. b modulo m for every (b, m) in the list
def garner_tcr(system):
    # compute products, a list signifying
    # products[i - 1] = m_1 * m_2 * ... * m_i
    products = [0 for _ in range(len(system))]
    products[0] = system[0][1]
    for i in range(1, len(system)):
        products[i] = products[i - 1] * system[i][1]

    # compute inv, a list signifying
    # inv[i - 1] = (m_1 * m_2 * ... * m_i) ^ (-1) mod m_(i+1)
    inv = list()
    for i in range(len(system) - 1):
        _, m_i = system[i]
        _, m_i1 = system[i + 1]
        inv.append(pow(products[i] % m_i1, -1, m_i1))

    # compute x, a list signifying
    # x[i] = a solution satisfying
    # the first i congruences in the system
    x = [system[0][0]]
    for i in range(1, len(system)):
        b, m = system[i]
        alpha = (b - x[i - 1]) * inv[i - 1] % m
        new_x = x[i - 1] + alpha * products[i - 1]
        x.append(new_x)
    return x[-1]

class MultiprimeRSA:
    def __init__(self, p, q, r, e):
        self.p = p
        self.q = q
        self.r = r
        self.e = e
        self.n = p * q * r
        self.phi = (p - 1) * (q - 1) * (r - 1)
        self.d = pow(self.e, -1, self.phi)
        print(self.e * self.d % self.phi)

    def encrypt(self, x):
        return pow(x, self.e, self.n)

    def slow_decrypt(self, y):
        return pow(y, self.d, self.n)

    def fast_decrypt(self, y):
        # use Garner's algorithm
        # first compute dec(y) % k for k in (p, q, r)
        system = []
        for k in [self.p, self.q, self.r]:
            module = pow(y % k, self.d % (k - 1), k)
            system.append((module, k))

        # apply Garner's algorithm over the congruence system
        return garner_tcr(system)

p = nextprime(1 << 699)
# p = nextprime(1 << 20)
q = nextprime(p)
r = nextprime(q)
e = (1 << 16) + 1

rsa = MultiprimeRSA(p, q, r, e)
x = rd.randint(1, rsa.n - 1)
y = rsa.encrypt(x)
print(x, y)
start = time.time()
fast_res = rsa.fast_decrypt(y)
stop = time.time()
print(fast_res, stop - start)
start = time.time()
slow_res = rsa.slow_decrypt(y)
stop = time.time()
print(slow_res, stop - start)

# sys = [(2, 3), (3, 5), (4, 7)]
# print(garner_tcr(sys))