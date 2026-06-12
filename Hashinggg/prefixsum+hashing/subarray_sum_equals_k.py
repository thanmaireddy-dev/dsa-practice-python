def subarray_sum_equals_k(nums, k):
    n= len(nums)
    prefixsum=0
    seen={0:1}
    count=0
    for i in range(n):
        prefixsum= prefixsum + nums[i]
        needed= prefixsum-k
        if needed in seen:
            count= count+ seen[needed]
        if prefixsum in seen:
            seen[prefixsum]+=1
        else:
            seen[prefixsum]=1
    return count

print(subarray_sum_equals_k([1,2,3], 3))
    