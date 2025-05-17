from sympy import isprime, randprime

def factorize(n):
    fact = []
    pows = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            fact.append(d)
            pows.append(0)
        while n % d == 0:
            pows[-1] += 1
            n //= d
        d += 1
    if n > 1:
        fact.append(n)
        pows.append(1)
    return fact, pows

def get_generator(p, fact):
    # p prime
    # returns a generator element of the group Zp
    phi = p - 1
    for g in range(2, p):
        # is g a generator of Zp?
        # phi = p1^e1 * p2^e2 * ... * pk^ek
        # g is a generator if g^(phi(p) / pi) != 1, i = 1, ..k

        for factor in fact:
            if pow(g, phi // factor, p) == 1:
                break
        else:
            return g
    return None

def generate_smooth_prime(bit_length=1024, max_factor_bits=16):
    # Try different sets of small primes until we find a good one
    while True:
        factors = [2]
        current_product = 2  # start with 2 to ensure even p - 1
        while current_product.bit_length() < bit_length - 20:
            q = randprime(10000, 2 ** max_factor_bits)
            if q not in factors:  # avoid duplicates
                factors.append(q)
                current_product *= q

        # Try small odd multipliers k to get a candidate p
        for k in range(1, 10000, 2):
            if k not in factors:
                p_candidate = current_product * k + 1
                if p_candidate.bit_length() >= bit_length and isprime(p_candidate):
                    k_fact, k_pow = factorize(k)
                    return p_candidate, sorted(factors + k_fact), k_pow + [1 for _ in range(len(factors))]