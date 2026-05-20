def three_sum_closest(nums, target):
    n= len(nums)
    nums.sort()
    closest_sum= nums[0]+ nums[1]+ nums[2]
    for i in range(n):
        p1= i+1
        p2= n-1
        while (p1<p2):
            currsum= nums[i] + nums[p1]+ nums[p2]
            if currsum== target:
                return currsum
            elif abs(target-currsum)< abs(target- closest_sum):
                closest_sum= currsum
                
            if currsum< target:
                p1=p1+1
            else:
                p2=p2-1
    return closest_sum


print(three_sum_closest([-1,2,1,-4],1))