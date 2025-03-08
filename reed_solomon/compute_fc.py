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
    res = 1
    # for _ in range(p - 2):
    #     res = res * a % p
    # return res

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

def get_inverses(a, p):
    c = [a[0]]
    for i in range(1, len(a)):
        c.append(c[i - 1] * a[i] % p)
    u = mod_inv(c[-1], p)
    invs = [0 for _ in range(len(c))]
    for i in range(len(c) - 1, 0, -1):
        invs[i] = u * c[i - 1] % p
        u = u * a[i] % p
    invs[0] = u
    return invs


def fast_fc(A, z, p):
    invs = get_inverses([(j - i + p) % p for i in A for j in A if i != j], p)
    inv_idx = 0
    res = 0
    for i in A:
        zi = z[i - 1]
        for j in A:
            if i != j:
                zi = zi * j * invs[inv_idx] % p
                inv_idx = inv_idx + 1
        res = (res + zi) % p
    return res