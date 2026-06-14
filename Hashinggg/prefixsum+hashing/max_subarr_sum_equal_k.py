#geeks for geeks
def maximum_subarray_sum_equals_k(nums, k):
    n= len(nums)
    currsum= sum(nums[:k])
    maxsum= currsum
    left=0
    for right in range(k,n):
        currsum= currsum + nums[right]- nums[left]
        left= left+1
        maxsum= max(maxsum, currsum)
    return maxsum

print(maximum_subarray_sum_equals_k([100,200,300,400], 2))
        
    
    
    
    