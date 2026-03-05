def maximum_average_subarray_I(arr, k):
    n= len(arr)
    left=0
    max_sum= float('-inf')
    winsum= sum(arr[:k])
    for right in range(k,n):
        winsum= winsum+ arr[right]- arr[left]
        left= left+1
        max_sum= max(max_sum, winsum)
    return float(max_sum)/k

print(maximum_average_subarray_I([1,12,-5,-6,50,3],4))
    