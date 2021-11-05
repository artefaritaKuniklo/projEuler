#!/usr/bin/env python3
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

primeDict = {}
top = 20

def addPrime(p):
    if p in primeDict.keys():
        primeDict[p] += 1
    else:
        primeDict[p] = 1
    return

def mergeDict(D):
    for k, v in D.items():
        if k in primeDict.keys():
            primeDict[k] = max(v, primeDict[k])
        else:
            primeDict[k] = v
    return

def isPrime(n):
    res = True
    if n > 3:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                res = False
                break
    return res

def PF(N):
    PFDict = {}
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            while N % i == 0:
                N = N // i
                if i in PFDict.keys():
                    PFDict[i] += 1
                else:
                    PFDict[i] = 1
    if N != 1:
        i = N
        if i in PFDict.keys():
            PFDict[i] += 1
        else:
            PFDict[i] = 1
    return PFDict

for n in range(2, top+1):
    if isPrime(n):
        addPrime(n)
    else:
        mergeDict(PF(n))

SM = 1
for k, v in primeDict.items():
    SM *= k**v
print(SM)
