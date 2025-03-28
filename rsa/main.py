from sympy import nextprime
import random as rd
import time
from rsa.MultiprimeRSA import *
from rsa.MultipowerRSA import *
from rsa.expo import *

def dec_demo(rsa, samples = 1):
    fast_res, x = None, None
    fast_times, slow_times = 0, 0
    for _ in range(samples):
        x = rd.randint(1, rsa.n - 1)
        y = rsa.encrypt(x)
        start = time.time()
        fast_res, _ = rsa.fast_decrypt(y)
        fast_times += time.time() - start
        start = time.time()
        slow_res = rsa.slow_decrypt(y)
        slow_times += time.time() - start
    print(slow_times / samples, fast_times / samples, slow_times / fast_times)
    print(f'dec(enc(x) == x ? {fast_res == x}')

def expo_demo(rsa, beta, max_window, samples = 1):
    methods = {
        'binary_expo': (binary_exp, None),
        'fixed_window_expo': (fixed_window_expo, beta),
        'sliding_window_expo': (sliding_window_expo, max_window),
    }

    runtimes = {key: 0 for key in methods.keys()}
    avg_chain_lengths = {key: 0 for key in methods.keys()}

    for _ in range(samples):
        for name, (expo, extra_param) in methods.items():
            x = rd.randint(1, rsa.n - 1)
            y = rsa.encrypt(x)
            start = time.time()
            res, avg_chain_len = rsa.fast_decrypt(y, expo, extra_param)
            runtimes[name] += time.time() - start
            avg_chain_lengths[name] += avg_chain_len

    for name, runtimes in runtimes.items():
        print(f'{name} : {avg_chain_lengths[name] / samples} : {runtimes / samples}')

if __name__ == '__main__':
    p = nextprime(1 << 699)
    # p = nextprime(1 << 20)
    q = nextprime(p)
    r = nextprime(q)
    e = (1 << 16) + 1

    multi_prime_rsa = MultiprimeRSA(p, q, r, e)
    multi_power_rsa = MultipowerRSA(p, q, e)

    dec_demo(multi_prime_rsa, 30)
    print('-' * 30)
    dec_demo(multi_power_rsa, 30)
    print('-' * 30)
    print('-' * 30)
    expo_demo(multi_prime_rsa, 8, 7, 30)