#!/usr/bin/env python3
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

sum = 2
a = 1
b = 2
top = 4000000
while a+b <= top:
    if (a+b) % 2 == 0:
        sum += a+b
    print(a+b)
    a, b = b, a+b
print(sum)