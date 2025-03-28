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
    x %= m
    bits = [int(bit) for bit in bin(e)[2:]]
    res = 1
    for bit in bits:
        res = res * res % m
        if bit:
            res = res * x
    return res



if __name__ == '__main__':
    print(binary_exp(5, 50, 1e40))