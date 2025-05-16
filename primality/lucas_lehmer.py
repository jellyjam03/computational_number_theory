import time

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

def reduce_modulo(a, n):
    m = (1 << n) - 1
    return a % m

def lucas_lehmer(n, reduction_func, samples = 10):
    if n == 2:
        return True

    if not naive_is_prime(n):
        return False

    u = 4
    for _ in range(n - 2):
        u = pow(u, 2) - 2
        u = reduction_func(u, n)

    return u == 0

if __name__ == '__main__':
    lucas_lehmer(3, reduce_mersenne)
    for x in range(20):
        if lucas_lehmer(x, reduce_mersenne) != naive_is_prime((1 << x) - 1):
            print(x)

    funcs = {"reduce modulo": reduce_modulo, "reduce mersenne": reduce_mersenne}
    for name, func in funcs.items():
        start = time.time()
        result = lucas_lehmer(1009, func)
        end = time.time()

        print(name, result, end - start)

