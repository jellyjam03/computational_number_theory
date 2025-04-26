from sympy import nextprime

from solovay_strassen import solovay_strassen
from lucas_lehmer import lucas_lehmer, naive_is_prime


if __name__ == '__main__':
    p = nextprime(1 << 699)
    np = p - 2

    print(p, np)

    false_positives = 0
    false_negatives = 0

    nr_samples = 100
    for _ in range(nr_samples):
        if not solovay_strassen(p):
            false_negatives += 1
        if solovay_strassen(np):
            false_positives += 1

    print(f"False positive rate: {false_positives / nr_samples}")
    print(f"False negative rate: {false_negatives / nr_samples}")

