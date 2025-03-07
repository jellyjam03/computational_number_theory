from sympy import nextprime
import sys
import numpy as np
from itertools import combinations

def convert_base(x, p) -> list:
    res = []
    while x:
        res.append(x % p)
        x //= p
    return res[::-1]

def partition_string(m, block_size):
    res = []
    for i in range(0, len(m), block_size):
        yi = m[i]
        for j in range(i + 1, i + block_size):
            # no need for modulo
            # p has been chosen s.t. yi < p
            yi = (yi << 8) + m[j]
        res.append(yi)
    return res


def evaluate_poly(coefficients, x, p):
    res = 0
    for coeff in coefficients:
        res = ((res + coeff) * x) % p
    return res

def encode(m, p, block_size, s, is_number = False) -> (list, list):
    # m - message
    # p - agreed prime (161 bits)
    # s - maximum number of expected errors

    a = convert_base(m, p) if is_number else partition_string(m, block_size)
    y = []
    for i in range(1, len(a) + 1 + 2 * s + 1):
        y.append(evaluate_poly(a, i, p))
    return a, y

def log_exp(x, k, p):
    if k == 0:
        return 1
    if k == 1:
        return x
    sq_x = log_exp(x, k // 2, p)
    if k % 2 == 0:
        return sq_x * sq_x % p
    return sq_x * sq_x * x % p


def mod_inv(a, p):
    if a < p:
        a += p
    # compute a ** (p - 2)
    return log_exp(a, p - 2, p)

def slow_fc(A, z, p):
    res = 0
    for i in A:
        zi = z[i - 1]
        for j in A:
            if i != j:
                inv = mod_inv(j - i, p)
                zi = zi * j * inv % p
        res = (res + zi) % p
    return res

def medium_fc(A, z, p):
    res = 0
    for i in A:
        zi = z[i - 1]
        hi, lo = 1, 1
        for j in A:
            if i != j:
                hi = (hi * j) % p
                lo = (lo * (j - i + p)) % p
                # inv = mod_inv(j - i, p)
                # zi = zi * j * inv % p
        inv = mod_inv(lo, p)
        res = (res + (zi * hi * inv) % p) % p
    return res

def fast_fc(A, z, p):
    pass


def reconstruct_poly(A, p):
    pass

def decode(z, s, compute_fc, p):
    k = len(z) - 2 * s
    for A in combinations([i for i in range(1, len(z) + 1)], k):
        fc = compute_fc(A, z, p)
        if fc:
            continue
        # fc is 0
        print(A)
        return reconstruct_poly(A, p)

def add_noise(y, s):
    for i in range(s):
        y[i] ^= 2

(a, enc) = encode(29, 11, 1, 1, is_number=True)
print(a, enc)

add_noise(enc, 1)
print(enc)

decode(enc, 1, medium_fc, 11)

# chars = [0b000, 0b001, 0b000, 0b111]
# (a, enc) = encode(chars, 11, 2, 1, is_number=False)
# print(enc)