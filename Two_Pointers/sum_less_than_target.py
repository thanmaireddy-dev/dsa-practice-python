def count_pairs_whose_sum_is_less_than_target(nums, target):
    n= len(nums)
    if n<2:
        return 0
    nums.sort()
    p1=0
    p2=n-1
    count=0
    while (p1<p2):
        summ= nums[p1]+ nums[p2]
        if summ>= target:
            p2=p2-1
        else:
            count= count+ (p2-p1)
            p1=p1+1
    return count

print(count_pairs_whose_sum_is_less_than_target([-6,2,5,-2,-7,-1,3], -2))
    