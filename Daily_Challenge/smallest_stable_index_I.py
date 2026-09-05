def firstStableIndex_I(nums, k):
        n= len(nums)
        leftmax=[0]*n
        rightmin=[0]*n
        leftmax[0]= nums[0]
        rightmin[n-1]= nums[n-1]
        for i in range(1,n):
            leftmax[i]= max(leftmax[i-1],nums[i])
        for i in range(n-2,-1,-1):
            rightmin[i]= min(rightmin[i+1], nums[i])
        for i in range(n):
            stability= leftmax[i]-rightmin[i]
            if stability<=k:
                return i
        return -1

print(firstStableIndex_I([5,0,1,4],3))