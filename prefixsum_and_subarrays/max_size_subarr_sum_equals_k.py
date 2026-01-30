def maximum_size_subarray_sum_equals_k(arr,k):
    n= len(arr)
    prefixsum=0
    seen= {0:-1}
    maxlen= 0
    for i in range(n):
        prefixsum= prefixsum+ arr[i]
        needed= prefixsum-k
        if needed in seen:
            length= i- seen[needed]
            maxlen= max(length, maxlen)
        if prefixsum not in seen:
            seen[prefixsum]=i
            
    return maxlen

print(maximum_size_subarray_sum_equals_k([2,3,4,-3,-1,3],2))