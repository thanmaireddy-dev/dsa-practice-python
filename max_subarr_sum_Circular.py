def maximum_subarray_sum_Circular(arr):
    n= len(arr)
    totalsum= sum(arr)
    
    maxsum= float('-inf')
    currmax=0
    
    minsum= float('inf')
    currmin=0
    
    for i in range(n):
        if currmax<0:
            currmax=0
        currmax= currmax+ arr[i]
        maxsum= max(maxsum, currmax)
        
        if currmin>0:
            currmin=0
        currmin= currmin+ arr[i]
        minsum= min(minsum, currmin)
        
    if maxsum<0:
        return maxsum
             
    return max(maxsum, totalsum-minsum )

print(maximum_subarray_sum_Circular([5,-3,5]))
        