def finalPrices(nums):
    n= len(nums)
    result=[0]*n
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and stack[-1]>nums[i]:
            stack.pop()
        if not stack:
            result[i]= nums[i]
        elif stack[-1]<=nums[i]:
            result[i]=nums[i]-stack[-1]
        stack.append(nums[i])
    return result

print(finalPrices([10,1,1,6]))