def replace_elements(nums):
    n=len(nums)
    if n==1:
        return [-1]
    result=[-1,nums[n-1]]
    for i in range(n-2,0,-1):
        if nums[i]>=result[-1]:
            result.append(nums[i])
        else:
            result.append(result[-1])
    return result[::-1]

print(replace_elements([17,18,5,4,6,1]))