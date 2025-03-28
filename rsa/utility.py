# receive a list of tuples (b, m)
# meaning x congr. b modulo m for every (b, m) in the list
def garner_crt(system):
    # compute products, a list signifying
    # products[i - 1] = m_1 * m_2 * ... * m_i
    products = [0 for _ in range(len(system))]
    products[0] = system[0][1]
    for i in range(1, len(system)):
        products[i] = products[i - 1] * system[i][1]

    # compute inv, a list signifying
    # inv[i - 1] = (m_1 * m_2 * ... * m_i) ^ (-1) mod m_(i+1)
    inv = list()
    for i in range(len(system) - 1):
        _, m_i = system[i]
        _, m_i1 = system[i + 1]
        inv.append(pow(products[i] % m_i1, -1, m_i1))

    # compute x, a list signifying
    # x[i] = a solution satisfying
    # the first i congruences in the system
    x = [system[0][0]]
    for i in range(1, len(system)):
        b, m = system[i]
        alpha = (b - x[i - 1]) * inv[i - 1] % m
        new_x = x[i - 1] + alpha * products[i - 1]
        x.append(new_x)
    return x[-1]

def binary_exp(x, e, m):
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

def fixed_window_expo(x, e, beta, m):
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

def sliding_window_expo(x, e, w, m):
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


if __name__ == '__main__':
    print(sliding_window_expo(5, 15, 3, 1e15))