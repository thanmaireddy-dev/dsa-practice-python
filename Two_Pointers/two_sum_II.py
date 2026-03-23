def two_sum_sorted(nums, target):
    n= len(nums)
    sum=0
    p1=0
    p2= n-1
    while (p1<p2):
        sum= nums[p1]+ nums[p2]
        if sum== target:
            return [p1+1, p2+1]
        elif sum<target:
            p1=p1+1
        else:
            p2=p2-1
    return []

print(two_sum_sorted([2,3,4],6))
    