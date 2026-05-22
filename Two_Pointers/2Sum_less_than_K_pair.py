def two_sum_less_than_k_Pair(nums, target):
    n= len(nums)
    nums.sort()
    p1=0
    p2=n-1
    bestsum= -1
    bestpair=[-1, -1]
    if n<2:
        return [-1,-1]
    while (p1<p2):
        currsum= nums[p1]+ nums[p2]
        if currsum<target:
            if currsum> bestsum:
                bestsum= currsum
                bestpair= [nums[p1], nums[p2]]
            p1=p1+1
        else:
            p2=p2-1
    return bestpair


print(two_sum_less_than_k_Pair([2, 3, 4, 6, 8, 10], 10))