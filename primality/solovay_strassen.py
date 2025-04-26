import random as rd

def gcd_euler(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def legendre_jacobi(a, m):
    if gcd_euler(a, m) != 1:
        return 0

    if a == 1:
        return 1

    if a == 2:
        return 1 if m % 8 in {1, 7} else -1

    if a > m:
        return legendre_jacobi(a % m, m)

    if a < m and a % 2 == 1 and m % 2 == 1:
        return legendre_jacobi(m % a, a) * ((-1) if m % 4 == 3 and a % 4 == 3 else 1)

    s = 0
    while a % 2 == 0:
        a /= 2
        s += 1

    return legendre_jacobi(a, m) * (1 if s % 2 == 0 else legendre_jacobi(2, m))

def solovay_strassen(n, nr_samples = 10):
    if n < 3 or n % 2 == 0:
        print("Input must be an odd integer larger or equal to 3.\n")
        return None

    for _ in range(nr_samples):
        a = rd.randint(2, n - 2)
        symbol = legendre_jacobi(a, n)
        if symbol == -1:
            symbol = n - 1

        if symbol == 0 or pow(a, (n - 1) // 2, n) != symbol:
            # n is surely composite
            return False

    # if no contradiction of the primality of n was found
    # assume n is prime with a tiny error margin
    return True

if __name__ == '__main__':
    print(solovay_strassen(5393, 1))