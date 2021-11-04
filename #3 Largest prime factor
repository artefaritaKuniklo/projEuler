#!/usr/bin/env python3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def LPF(N):
    n = 2
    PFL = []
    while n <= N:
        if N % n == 0 and isPrime(n):
            N /= n
            PFL.append(n)
            n = 2
        n += 1
    return max(PFL)

print(LPF(600851475143))