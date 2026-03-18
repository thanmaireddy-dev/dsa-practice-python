def reverse_an_array(nums):
    n= len(nums)
    p1=0
    p2= n-1
    while (p1<p2):
        nums[p1], nums[p2]= nums[p2], nums[p1]
        p1=p1+1
        p2=p2-1
    return nums 

print(reverse_an_array([1,2,3,4,5,6,7,8]))