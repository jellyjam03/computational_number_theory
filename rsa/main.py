from sympy import nextprime
import random as rd
import time
from MultiprimeRSA import *
from MultipowerRSA import *

p = nextprime(1 << 699)
# p = nextprime(1 << 20)
q = nextprime(p)
r = nextprime(q)
e = (1 << 16) + 1


def multi_prime_demo():
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

def multi_power_demo():
    rsa = MultipowerRSA(p, q, e)
    x = rd.randint(1, rsa.n - 1)
    y = rsa.encrypt(x)
    print(x, y)
    start = time.time()
    fast_res = rsa.fast_decrypt(y)
    print(time.time() - start, fast_res)
    start = time.time()
    slow_res = rsa.slow_decrypt(y)
    print(time.time() - start, slow_res)

multi_power_demo()