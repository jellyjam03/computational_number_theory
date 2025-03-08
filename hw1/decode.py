from itertools import combinations
import numpy as np
from compute_fc import get_inverses

def reconstruct_poly(A, z, p):
    invs = get_inverses([(i - j + p) % p for i in A for j in A if i != j], p)
    invs_idx = 0
    poly = np.zeros((len(A)))
    for i in A:
        add = np.zeros_like(poly)
        add[0] = z[i - 1]
        for j in A:
            if i != j:
                add *= invs[invs_idx]
                invs_idx += 1
                add %= p

                # multiply with (x + (p - j))
                # add * x + add * (p - j)
                # here we shift 1 position to the left
                temp = np.roll(add, 1)
                # now we multiply by p - j
                add *= (p - j)
                add += temp
                add %= p
        poly += add
        poly %= p
    return poly.tolist()[::-1]

def decode(z, s, compute_fc, p):
    k = len(z) - 2 * s
    for A in combinations([i for i in range(1, len(z) + 1)], k):
        fc = compute_fc(A, z, p)
        if fc:
            continue
        # fc is 0
        return reconstruct_poly(A, z, p)