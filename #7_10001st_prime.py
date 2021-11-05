# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

counter = 1
prime = 2

def isPrime(n):
    res = True
    if n > 2:
        for i in range(2, int(n**0.5)+1):
            if n%i == 0:
                res = False
                break
    return res

while counter < 10002:
    while not isPrime(prime):
        prime += 1
    print(f"{counter}\t{prime}")
    counter += 1
    prime += 1