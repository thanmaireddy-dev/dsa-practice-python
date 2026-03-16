def longest_zero_sum_subarray(arr):
    n= len(arr)
    seen={0:-1}
    maxlen=0
    prefixsum=0
    for i in range(n):
        prefixsum= prefixsum + arr[i]
        if prefixsum in seen:
            length= i- seen[prefixsum]
            maxlen= max(maxlen, length)
        else:
            seen[prefixsum]= i
    return maxlen

print(longest_zero_sum_subarray([2,3,-5,0,-3,6]))      
    
    
    