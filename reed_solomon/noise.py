def add_noise(y, s):
    for i in range(s):
        y[i + 4] ^= 2