def remove_element(nums, val):
    n= len(nums)
    p1=0
    for i in range(n):
        if nums[i]!= val:
            nums[p1]= nums[i]
            p1=p1+1
    return p1

print(remove_element([0,1,2,2,3,0,4,2],2))
        