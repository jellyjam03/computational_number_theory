from sympy import nextprime
import random as rd
import time
from MultiprimeRSA import *
from MultipowerRSA import *

def demo(rsa, samples = 1):
    fast_res, x = None, None
    fast_times, slow_times = 0, 0
    for _ in range(samples):
        x = rd.randint(1, rsa.n - 1)
        y = rsa.encrypt(x)
        start = time.time()
        fast_res = rsa.fast_decrypt(y)
        fast_times += time.time() - start
        start = time.time()
        slow_res = rsa.slow_decrypt(y)
        slow_times += time.time() - start
    print(slow_times / samples, fast_times / samples, slow_times / fast_times)
    print(f'dec(enc(x) == x ? {fast_res == x}')

if __name__ == '__main__':
    p = nextprime(1 << 699)
    # p = nextprime(1 << 20)
    q = nextprime(p)
    r = nextprime(q)
    e = (1 << 16) + 1

    multi_prime_rsa = MultiprimeRSA(p, q, r, e)
    multi_power_rsa = MultipowerRSA(p, q, e)
    demo(multi_prime_rsa, 30)
    print('-' * 30)
    demo(multi_power_rsa, 30)