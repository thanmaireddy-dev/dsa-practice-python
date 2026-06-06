def happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        summ = 0
        for digit in str(n):
            summ += int(digit) ** 2
        n = summ
    return n == 1

print(happy_number(19))