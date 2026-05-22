def maximum_no_of_k_sum_pairs(nums, k):
    n= len(nums)
    nums.sort()
    if n<2:
        return 0
    p1=0
    p2=n-1
    result= set()
    while (p1<p2):
        summ= nums[p1]+ nums[p2]
        if summ<k:
            p1=p1+1
        elif summ> k:
            p2=p2-1
        else:
            result.add((p1,p2))
            p1=p1+1
            p2=p2-1
    return len(result)

print(maximum_no_of_k_sum_pairs([3,1,3,4,3],6))