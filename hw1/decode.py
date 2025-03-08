from itertools import combinations
from compute_fc import get_inverses
from collections import deque

def reconstruct_poly(A, z, p):
    invs = get_inverses([(i - j + p) % p for i in A for j in A if i != j], p)
    invs_idx = 0
    poly = [0] * len(A)
    for i in A:
        add = [0] * len(A)
        add[0] = z[i - 1]
        for j in A:
            if i != j:
                add = [x * invs[invs_idx] for x in add]
                invs_idx += 1
                add = [x % p for x in add]

                # multiply with (x + (p - j))
                # add * x + add * (p - j)
                # here we shift 1 position to the left

                # temp = np.roll(add, 1)
                temp = deque(add)
                temp.rotate(1)
                # now we multiply by p - j
                add = [x * (p - j) for x in add]
                add = [add[k] + temp[k] for k in range(len(add))]
                add = [x % p for x in add]
        poly = [poly[k] + add[k] for k in range(len(poly))]
        poly = [x % p for x in poly]
    return poly[::-1]

def decode(z, s, compute_fc, p):
    k = len(z) - 2 * s
    for A in combinations([i for i in range(1, len(z) + 1)], k):
        fc = compute_fc(A, z, p)
        if fc:
            continue
        # fc is 0
        return reconstruct_poly(A, z, p)