def longest_subarray_with_sum_equals_zero(arr):
    n= len(arr)
    seen= {0:-1}
    prefixsum=0
    maxlen= float('-inf')
    for i in range (n):
        prefixsum= prefixsum+ arr[i]
        if prefixsum in seen:
            result= i- seen[prefixsum]
            maxlen= max(maxlen, result)
        else:
            seen[prefixsum]=i
    return maxlen

print(longest_subarray_with_sum_equals_zero([2,3,-5,0,3,-3,6 ]))
    
    
    