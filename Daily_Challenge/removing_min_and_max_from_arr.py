def minimumDeletions(nums):
    n=len(nums)
    minind= nums.index(min(nums))
    maxind= nums.index(max(nums))
    i= min(minind,maxind)
    j= max(minind,maxind)
    
    del1= j+1
    del2= n-i
    del3= (i+1) + (n-j)
    return min(del1, del2, del3)   

print(minimumDeletions([0,-4,19,1,8,-2,-3,5]))