def move_zeroes(nums):
    n= len(nums)
    p1=0
    for i in range(n):
        if nums[i]!=0:
            nums[p1]= nums[i]
            p1=p1+1
    while (p1<n):
        nums[p1]=0
        p1=p1+1
    return nums

print(move_zeroes([2,0,2,0,5,-1,0,0,4]))