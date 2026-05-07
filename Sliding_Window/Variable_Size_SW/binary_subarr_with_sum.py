def binary_subarrays_with_sum(nums, goal):
    n= len(nums)
    count=0
    prefixsum=0
    seen= {0:1}
    for i in range(n):
        prefixsum= prefixsum+ nums[i]
        needed= prefixsum-goal
        if needed in seen:
            count= count+ seen[needed]
        if prefixsum in seen:
            seen[prefixsum]+=1
        else:
            seen[prefixsum]=1
    return count


#literally the same problem as Subarray sum equals k