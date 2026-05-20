def two_sum_less_than_k(nums, target):
    n= len(nums)
    nums.sort()
    p1=0
    p2=n-1
    bestsum= -1
    if n<2:
        return -1
    while (p1<p2):
        currsum= nums[p1]+ nums[p2]
        if currsum<target:
            if currsum> bestsum:
                bestsum= currsum
            p1=p1+1
        else:
            p2=p2-1
    return bestsum


print(two_sum_less_than_k([2,7,11,15], 24))
    
    