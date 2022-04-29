# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math


def check_prime(x):
    '''
    check x is a prime
    '''
    is_prime = True
    for i in range(2, math.ceil(math.sqrt(x))+1):
        if x % i == 0:
            is_prime = False
            break
    return is_prime


sum = 2
for n in range(3, 2000000):
    if check_prime(n):
        sum += n

print(sum)
