def subarray_sum_equals_zeroBruteforce(arr):
    n= len(arr)
    for i in range(n):
        currsum=0
        for j in range(i,n):
            currsum= currsum+ arr[j]
            if currsum==0:
                return True
    return False

print(subarray_sum_equals_zeroBruteforce([5,10,2,3,4,-9,4,3]))
        