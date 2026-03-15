def minimum_size_subarray_sum(nums, target):
    n= len(nums)
    minlen=float('inf')
    left=0
    summ=0
    for right in range(n):
        summ= summ+ nums[right]
        while summ>= target:
            summ= summ- nums[left]
            minlen= min(minlen, right-left+1)
            left= left+1
    return minlen if minlen!=float('inf') else 0

print(minimum_size_subarray_sum([1,4,4],4))
        