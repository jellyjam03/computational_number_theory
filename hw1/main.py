from sympy import nextprime

def convert_base(x, p) -> list:
    res = []
    while x:
        res.append(x % p)
        x //= p
    return res[::-1]

def evaluate_poly(coefficients, x, p):
    res = 0
    for coeff in coefficients:
        res = ((res + coeff) * x) % p
    return res

def encode(m, p, block_size, s) -> list:
    # m - message
    # p - agreed prime (161 bits)
    # s - maximum number of expected errors

    a = convert_base(m, p)
    y = []
    for i in range(1, len(a) + 1 + 2 * s + 1):
        y.append(evaluate_poly(a, i, p))
    return y

enc = encode(29, 11, 1, 1)
print(enc)

def decode():
    pass

def add_noise():
    pass