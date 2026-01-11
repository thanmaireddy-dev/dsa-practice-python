def equi_index(arr):
    leftsum=0
    totalsum= sum(arr)
    for i, num in enumerate(arr):
        rightsum= totalsum-leftsum-num
        if leftsum== rightsum:
            return i
        leftsum= leftsum+ num
    return -1
        
print(equi_index([103,-1,99, 4]))
    