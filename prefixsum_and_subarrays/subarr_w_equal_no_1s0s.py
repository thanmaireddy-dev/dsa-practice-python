def contiguous_subarray_with_equal_num_of_0s_and_1s(arr):
    n= len(arr)
    maxlen= 0
    prefixsum=0
    seen= {0:-1}
    for i in range(n):
        if arr[i]==0:
            arr[i]=-1

        prefixsum= prefixsum+ arr[i]
        if prefixsum in seen:
            length= i- seen[prefixsum]
            maxlen= max(length, maxlen)
        else:
            seen[prefixsum]=i
    return maxlen

print(contiguous_subarray_with_equal_num_of_0s_and_1s([0,1,1,1,1,1,0,0,0]))