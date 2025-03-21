from utility import garner_crt

class MultiprimeRSA:
    def __init__(self, p, q, r, e):
        self.p = p
        self.q = q
        self.r = r
        self.e = e
        self.n = p * q * r
        self.phi = (p - 1) * (q - 1) * (r - 1)
        self.d = pow(self.e, -1, self.phi)
        print(self.e * self.d % self.phi)

    def encrypt(self, x):
        return pow(x, self.e, self.n)

    def slow_decrypt(self, y):
        return pow(y, self.d, self.n)

    def fast_decrypt(self, y):
        # use Garner's algorithm
        # first compute dec(y) % k for k in (p, q, r)
        system = []
        for k in [self.p, self.q, self.r]:
            module = pow(y % k, self.d % (k - 1), k)
            system.append((module, k))

        # apply Garner's algorithm over the congruence system
        return garner_crt(system)