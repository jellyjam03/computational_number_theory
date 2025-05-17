import random as rd
from random import randint

from rsa.utility import garner_crt
from discrete_log.utility import generate_smooth_prime
from discrete_log.utility import get_generator, factorize

# use Silver-Pohlig-Hellman algotithm to find log_alpha(beta) modulo p

def naive_discrete_log(alpha, beta, p, p_i):
    res = 1
    # in our use case, alpha has order of p_i
    # so the complexity is significantly smaller
    for i in range(p_i):
        if res == beta:
            return i
        res = (res * alpha) % p
    return None


def sph(alpha, beta, p, fact, pows):
    system = []
    # fact, pows = factorize(p - 1)
    # build the number s
    for p_i, e_i in zip(fact, pows):
        alpha_i = pow(alpha, (p - 1) // p_i, p)
        # s = c_(e_i-1) * p_i ^ (e_i - 1) + ... + c_1 * p_i ^ (e_1 - 1) + c_0
        s = 0
        c = []
        pow_p_i = p_i
        for j in range(e_i):
            E = (pow(beta, (p - 1) // pow_p_i, p) * pow(alpha, -((p - 1) * s) // pow_p_i, p)) % p
            c.append(naive_discrete_log(alpha_i, E, p, p_i))
            s = s + c[-1] * (pow_p_i // p_i)
            pow_p_i *= p_i
        system.append((s, pow_p_i // p_i))
    return garner_crt(system)

if __name__ == '__main__':
    # n = 11111111111111111111111
    # fact, pows = factorize(n - 1)
    # print(fact, pows)
    # alph = get_generator(n, fact)
    # beta = randint(2, n - 1)
    # eps = sph(alph, beta, n, fact, pows)
    # print(alph, beta)
    # print(eps)
    # print(pow(alph, eps, n))
    # print(sph(6, 5, 41, [2, 5], [3, 1]))

    p, fact, pows = generate_smooth_prime()
    alpha = get_generator(p, fact)
    beta = rd.randint(2, p)

    epsilon = sph(alpha, beta, p, fact, pows)
    print(epsilon)
    print(beta, pow(alpha, epsilon, p))