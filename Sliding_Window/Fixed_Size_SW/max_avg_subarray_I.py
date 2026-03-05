def maximum_average_subarray_I(arr,k):
    n= len(arr)
    left=0
    max_sum= float('-inf')
    winsum= sum(arr[:k])
    max_sum= max(winsum, max_sum)
    for right in range(k,n):
        winsum= winsum+ arr[right]- arr[left]
        max_sum= max(max_sum, winsum)
        left= left+1
        
    return float(max_sum)/k

print(maximum_average_subarray_I([1,12,-5,-6,50,3],4))