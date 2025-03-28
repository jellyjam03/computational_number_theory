from utility import garner_crt

class MultipowerRSA:
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.e = e
        self.n = p * p * q
        self.phi = p * (p - 1) * (q - 1)
        self.d = pow(self.e, -1, self.phi)

    def encrypt(self, x):
        return pow(x, self.e, self.n)

    def slow_decrypt(self, y):
        return pow(y, self.d, self.n)

    def fast_decrypt(self, y):
        # n = p^2 * q
        system = []
        x_q = pow(y % self.q, self.d % (self.q - 1), self.q)
        system.append((x_q, self.q))

        x0_p = pow(y % self.p, self.d % (self.p - 1), self.p)
        E = (y - pow(x0_p, self.e, self.p ** 2)) // self.p
        F = pow(x0_p, self.e - 1, self.p ** 2)

        x1_p = E * pow(self.e * F % self.p, -1, self.p) % self.p
        x_p = x1_p * self.p + x0_p
        system.append((x_p, self.p ** 2))

        # none is because addition chain support
        # was not added for multi power implementation
        return garner_crt(system), None