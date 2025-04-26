def naive_is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def lucas_lehmer(n, samples = 10):
    pass

if __name__ == '__main__':
    pass