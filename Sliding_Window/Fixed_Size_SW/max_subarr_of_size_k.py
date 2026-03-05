def maximum_subarray_of_size_k(arr,k):
    n= len(arr)
    left=0
    max_sum= float('-inf')
    winsum= sum(arr[:k])
    max_sum= max(max_sum, winsum)
    for right in range(k,n):
        winsum= winsum+ arr[right]- arr[left]
        left= left+1
        max_sum= max( max_sum, winsum)
        
    return max_sum


print(maximum_subarray_of_size_k([2,1,5,1,3,2],3))
        
                   
    