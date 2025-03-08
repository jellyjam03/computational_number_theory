def convert_base(x, p) -> list:
    res = []
    while x:
        res.append(x % p)
        x //= p
    return res[::-1]

def partition_string(m, block_size):
    res = []
    for i in range(0, len(m), block_size):
        yi = m[i]
        for j in range(i + 1, i + block_size):
            # no need for modulo
            # p has been chosen s.t. yi < p
            yi = (yi << 8) + m[j]
        res.append(yi)
    return res


def evaluate_poly(coefficients, x, p):
    res = 0
    for coeff in coefficients:
        res = ((res + coeff) * x) % p
    return res

def encode(m, p, block_size, s, is_number = False) -> (list, list):
    # m - message
    # p - agreed prime (161 bits)
    # s - maximum number of expected errors

    a = convert_base(m, p) if is_number else partition_string(m, block_size)
    y = []
    for i in range(1, len(a) + 1 + 2 * s + 1):
        y.append(evaluate_poly(a, i, p))
    return a, y