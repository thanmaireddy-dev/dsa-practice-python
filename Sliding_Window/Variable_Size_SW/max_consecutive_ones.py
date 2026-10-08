def longestOnes(nums, k):
    left=0
    maxlen=0
    count=0
    n= len(nums)
    for right in range(n):
        if nums[right]==0:
            count=count+1
        while count>k:
            if nums[left]==0:
                count=count-1
            left=left+1
        maxlen= max(maxlen, right-left+1)
    return maxlen

print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))