def two_sum(nums, target):
    seen={}
    for i,num in enumerate(nums):
        complement= target-num
        if complement in seen:
            return[i, seen[complement]]
        seen[num]= i

print(two_sum([2,3,4,1,5], 6))