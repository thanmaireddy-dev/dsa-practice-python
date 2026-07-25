def max_product(n):
    digits= [int(x) for x in str(n)]
    digits.sort()
    return digits[-1] * digits[-2]

print(max_product(124))