def three_sum(nums):
    n= len(nums)
    nums.sort()
    result= set()
    for i in range(n):
        p1= i+1
        p2= n-1
        while (p1<p2):
            currsum= nums[i] + nums[p1] + nums[p2]
            if currsum<0:
                p1=p1+1
            elif currsum>0:
                p2=p2-1
            else:
                result.add((nums[i], nums[p1], nums[p2]))
                p1=p1+1
                p2=p2-1
    return [list(t) for t in result]


print(three_sum([-1,0,1,2,-1,-4]))
            
        