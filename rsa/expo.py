def binary_exp(x, e, m, _):
    if x == 1 or x == 0:
        return x

    x %= m
    bits = [int(bit) for bit in bin(e)[2:]]
    add_chain = []
    res = 1
    for bit in bits:
        res = res * res % m
        if res > 1:
            add_chain.append(add_chain[-1] * 2)
        if bit:
            res = res * x % m
            if len(add_chain) != 0:
                add_chain.append(add_chain[-1] + 1)
            else:
                add_chain.append(1)

    return res, add_chain

def to_base_beta(x, beta):
    beta_digits = []
    cx = x
    while cx:
        beta_digits.append(cx % beta)
        cx = cx // beta
    return beta_digits[::-1]

def fixed_window_expo(x, e, m, beta):
    if x == 1 or x == 0:
        return x

    x %= m
    x_pow = [1]
    add_chain = []
    for i in range(1, beta):
        x_pow.append(x_pow[-1] * x % m)
        add_chain.append(i)

    beta_digits = to_base_beta(e, beta)
    res = 1
    current_pow = 0
    for digit in beta_digits:
        res = res ** beta % m
        current_pow = current_pow * beta
        if current_pow > add_chain[-1]:
            add_chain.append(current_pow)
        res = res * x_pow[digit] % m
        current_pow = current_pow + digit
        if current_pow > add_chain[-1]:
            add_chain.append(current_pow)
    return res, add_chain

def sliding_window_expo(x, e, m, w):
    if x == 1 or x == 0:
        return x

    x %= m
    x_pow = [0 for _ in range((1 << w))]
    x_pow[:3] = [1, x, x * x % m]

    add_chain = [1, 2]
    for q in range(3, (1 << w), 2):
        x_pow[q] = x_pow[q - 2] * x_pow[2] % m
        add_chain.append(q)

    bits = [int(bit) for bit in bin(e)[2:]]

    res = 1
    i = 0
    current_pow = 0
    while i < len(bits):
        if bits[i] == 0:
            res = res * res % m
            current_pow *= 2
            if current_pow > add_chain[-1]:
                add_chain.append(add_chain[-1] * 2)
            i += 1
        else:
            j = min(i + w - 1, len(bits) - 1)
            while j > i:
                if bits[j] == 1:
                    break
                j -= 1
            window = bits[i : j + 1]
            w_length = j - i + 1
            w_value = int(''.join(map(str, window)), 2)

            res = res ** (1 << w_length) % m
            current_pow *= (1 << w_length)
            if current_pow > add_chain[-1]:
                add_chain.append(current_pow)
            res = res * x_pow[w_value] % m
            current_pow = current_pow + w_value
            if current_pow > add_chain[-1]:
                add_chain.append(current_pow)

            i = j + 1

    return res, add_chain

def default_expo(x, e, m, _):
    return pow(x, e, m), []

if __name__ == '__main__':
    print(sliding_window_expo(5, 15, 3, 1e15))