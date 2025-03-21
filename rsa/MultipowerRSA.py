from utility import garner_crt

class MultipowerRSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e
        self.n = p * p * q
        self.phi = p * (p - 1) * (q - 1)
        self.d = pow(self.e, -1, self.phi)
        print(self.e * self.d % self.phi)

    def encrypt(self, x):
        return pow(x, self.e, self.n)

    def slow_decrypt(self, y):
        return pow(y, self.d, self.n)

    def fast_decrypt(self, y):
        # n = p^2 * q
        system = []
        pass