def maxAlternatingSum(nums):
    ans=0
    n= len(nums)
    for i in range(n):
        nums[i]= nums[i]*nums[i]
    nums.sort()
    for i in range(0, n//2):
        ans= ans-nums[i]
    for i in range(n//2, n):
        ans=ans+nums[i]
    return ans

print(maxAlternatingSum([1,2,3]))