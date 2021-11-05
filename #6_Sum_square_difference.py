# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

a = []
sum = 0
for i in range(100):
    a.append(i+1)
for ind_a, ax in enumerate(a):
    for ind_b, bx in enumerate(a):
        if ind_a != ind_b:
            sum += (ax*bx)
print(sum)
