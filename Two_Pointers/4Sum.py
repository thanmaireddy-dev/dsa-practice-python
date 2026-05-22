def four_sum(nums, target):
    n= len(nums)
    nums.sort()
    result= set()
    for i in range(n):
        for j in range(i+1, n):
            p1=j+1
            p2=n-1
            while (p1<p2):
                summ= nums[i]+ nums[j]+ nums[p1]+ nums[p2]
                if summ< target:
                    p1=p1+1
                elif summ> target:
                    p2=p2-1
                else:
                    result.add((nums[i], nums[j], nums[p1], nums[p2]))
                    p1=p1+1
                    p2=p2-1
    return [list(t) for t in result]

print(four_sum([1,0,-1,0,-2,2],0))