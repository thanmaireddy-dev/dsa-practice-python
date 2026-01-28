def Maximum_Size_Subarray_Sum_Equals_K(arr,k):
    n= len(arr)
    maxlen=0
    prefixsum=0
    seen= {0:-1}
    for i in range (n):
        prefixsum= prefixsum + arr[i]
        needed= prefixsum-k
        if needed in seen:
            length= i- seen[needed]
            maxlen= max(maxlen, length)
        if prefixsum not in seen:
            seen[prefixsum]=i
    return maxlen

print(Maximum_Size_Subarray_Sum_Equals_K([2, -1, 2, 1],3))
            
        
    