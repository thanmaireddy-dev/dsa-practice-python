def maximum_absolute_sum_of_any_subarray (arr):
    n= len(arr)
    
    maxsum=float('-inf')
    currmax=0
    
    minsum= float('inf')
    currmin=0
    
    for i in range(n):
        if currmax<0:
            currmax=0
        currmax= currmax+ arr[i]
        maxsum= max(currmax, maxsum)
        
        if currmin>0:
            currmin=0
        currmin= currmin+ arr[i]
        minsum= min(currmin, minsum)
        
    return max(maxsum, abs(minsum))

print(maximum_absolute_sum_of_any_subarray([2,-1,3,-5,4,3]))