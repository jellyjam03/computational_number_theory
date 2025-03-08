from sympy import nextprime
from encode import encode
from noise import add_noise
from decode import decode
from compute_fc import slow_fc, medium_fc, fast_fc

(a, enc) = encode(29, 11, 1, 1, is_number=True)
print(a, enc)

add_noise(enc, 1)
print(enc)

res = decode(enc, 1, fast_fc, 11)
print(res)

# chars = [0b000, 0b001, 0b000, 0b111]
# (a, enc) = encode(chars, 11, 2, 1, is_number=False)
# print(enc)