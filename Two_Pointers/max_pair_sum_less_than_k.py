def maxSum(nums, k):
    n= len(nums)
    nums.sort()
    p1=0
    p2=n-1
    maxpair=[-1,-1]
    maxsum=0
    while (p1<p2):
        summ= nums[p1]+ nums[p2]
        if summ>=k:
            p2=p2-1
        else:
            if summ>maxsum:
                maxsum=summ
                maxpair=[nums[p1],nums[p2]]
            p1=p1+1
    return maxpair

print(maxSum([2, 4, 3, 6, 8, 10],10))