# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math


for a in list(range(1, 32)):
    max_bc = math.ceil(math.sqrt(1000-math.pow(a, 2)))
    for b in list(range(1, max_bc)):
        max_c = math.ceil(math.sqrt(1000-math.pow(a, 2)-math.pow(b, 2)))
        for c in list(range(1, max_c)):
            if a*a+b*b+c*c == 1000:
                print("%d %d %d" % (a, b, c))
