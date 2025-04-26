def naive_is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def reduce_mersenne(a, n):
    m = (1 << n) - 1

    # separate the number into 2 halves
    a0 = a & m
    a1 = a >> n

    # reduce the number modulo a
    a = a0 + a1
    if a > m:
        a -= m

    return a if a < m else 0

def lucas_lehmer(n, samples = 10):
    if n == 2:
        return True

    if not naive_is_prime(n):
        return False

    u = 4
    for _ in range(n - 2):
        u = pow(u, 2) - 2
        u = reduce_mersenne(u, n)

    return u == 0

if __name__ == '__main__':
    for x in range(60):
        if lucas_lehmer(x) != naive_is_prime((1 << x) - 1):
            print(x)