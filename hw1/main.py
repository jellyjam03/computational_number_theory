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

(a, enc) = encode(29, 11, 1, 1, is_number=True)
print(enc)

# chars = [0b000, 0b001, 0b000, 0b111]
# (a, enc) = encode(chars, 11, 2, 1, is_number=False)
# print(enc)

def slow_fc(A, p):
    pass

def medium_fc(A, p):
    pass

def fast_fc(A, p):
    pass


def reconstruct_poly(A, p):
    pass

def decode(y, s, compute_fc, p):
    k = len(y) - 2 * s
    for A in combinations(y, k):
        fc = compute_fc(A, p)
        if fc:
            continue
        # fc is 0
        return reconstruct_poly(A, p)

def add_noise(y, s):
    for i in range(s):
        y[i] ^= 1