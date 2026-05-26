def valid_triangle_number(nums):
    n= len(nums)
    nums.sort()
    count=0
    for i in range(n-1, 1, -1):
        p1=i-1
        p2=0
        while( p1>p2):
            if nums[p1]+ nums[p2]> nums[i]:
                count= count+ (p1-p2)
                p1=p1-1
            else:
                p2=p2+1
    return count

print(valid_triangle_number([2,2,3,4]))