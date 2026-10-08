def longestSubarray(nums):
    n= len(nums)
    count=0
    p1=p2=0
    maxlen=0
    for p1 in range(n):
        if nums[p1]==0:
            count+=1
        if count>1:
            if nums[p2]==0:
                count-=1
            p2=p2+1
        maxlen=max(maxlen,p1-p2)
    return maxlen

print(longestSubarray([0,1,1,1,0,1,1,0,1]))