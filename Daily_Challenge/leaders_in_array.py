def leaders(nums):
    n=len(nums)
    result=[nums[n-1]]
    for i in range(n-2,-1,-1):
        if nums[i]>=result[-1]:
            result.append(nums[i])
    return result[::-1]

print(leaders([16, 17, 4, 3, 5, 2]))