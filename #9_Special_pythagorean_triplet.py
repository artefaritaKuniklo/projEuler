# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

min_a = math.floor(math.sqrt(1000000/3))
max_a = math.ceil(math.sqrt(1000000))


for a in list(range(math.floor(math.sqrt(1000000/3)), math.ceil(math.sqrt(1000000)))):
    max_bc = 1000000 - math.pow(a, 2)
    for b in list(range(math.floor(math.sqrt(max_bc/2)), math.ceil(math.sqrt(max_bc)))):
        max_c = 1000000 - math.pow(a, 2) - math.pow(b, 2)
        for c in list(range(1, math.ceil(math.sqrt(max_c)))):
            if int(math.pow(a, 2) + math.pow(b, 2)+math.pow(c, 2)) == 1000000:
                print(math.pow(a, 2) + math.pow(b, 2)+math.pow(c, 2))
