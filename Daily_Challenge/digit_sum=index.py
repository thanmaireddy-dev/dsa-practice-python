def digit_sum(nums):
    for i,num in enumerate(nums):
        summ=0
        strr= str(num)
        for char in strr:
            summ= summ+ int(char)
        if summ==i:
            return i
    return -1

print(digit_sum([1,10,11]))