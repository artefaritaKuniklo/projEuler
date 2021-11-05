#!/usr/bin/env python3
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindromic(n):
    new = list(str(n))
    new.reverse()
    return n == int("".join(new))

candidateList = set()
for n in range(100*100, 999*999+1):
    if isPalindromic(n):
        for a in range(100, 1000):
            if n%a == 0 and 100 <= n/a <= 999:
                candidateList.add(n)

print(max(candidateList))
