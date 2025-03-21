from sympy import nextprime
from encode import encode
from noise import add_noise
from decode import decode
from compute_fc import slow_fc, medium_fc, fast_fc
import time

def compare_fc(m, p, block_size, s, is_number=False):
    (a, enc) = encode(m, p, block_size, s, is_number=is_number)
    print(f'The initial polynomial: {a}\nIts encoding: {enc}')

    add_noise(enc, s)

    fc_methods = {'slow_fc': slow_fc, 'medium_fc': medium_fc, 'fast_fc': fast_fc}
    print('fc calculation -- execution time -- result poly')
    for method in fc_methods:
        start_time = time.time()
        res = decode(enc, s, fc_methods[method], p)
        end_time = time.time()
        print(f'{method} -- {end_time - start_time} -- {res}')

def example():
    p = 11
    m = 29
    compare_fc(m, p, 1, 1, True)

def demo(filename, p, block_size, s):
    # retrieve message from m as array of bytes
    with open(filename, 'rb') as f:
        message = f.read()
        # m = partition_string(message, block_size)
        compare_fc(message, p, block_size, s)

p_161 = nextprime(1 << 160)

demo('./message.txt', p_161, 20, 3)
# example()