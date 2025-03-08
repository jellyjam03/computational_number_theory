from sympy import nextprime
from encode import encode
from noise import add_noise
from decode import decode
from compute_fc import slow_fc, medium_fc, fast_fc
import time

(a, enc) = encode(29, 11, 1, 1, is_number=True)
print(a, enc)

add_noise(enc, 1)
print(enc)

fc_methods = {'slow_fc': slow_fc, 'medium_fc': medium_fc, 'fast_fc': fast_fc}
print('fc calculation -- execution time -- result poly')
for method in fc_methods:
    start_time = time.time()
    res = decode(enc, 1, fc_methods[method], 11)
    end_time = time.time()
    print(f'{method} -- {end_time - start_time} -- {res}')

# res = decode(enc, 1, fast_fc, 11)
# print(res)

# chars = [0b000, 0b001, 0b000, 0b111]
# (a, enc) = encode(chars, 11, 2, 1, is_number=False)
# print(enc)