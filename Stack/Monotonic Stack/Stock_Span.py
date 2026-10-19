def calculateSpan(nums):
    n= len(nums)
    result=[0]*n
    stack=[0]
    for i in range(n):
        while stack and nums[stack[-1]]<=nums[i]:
            stack.pop()
        if not stack:
            result[i]=i+1
        elif nums[stack[-1]]>nums[i]:
            result[i]= i-stack[-1]
        stack.append(i)
    return result

print(calculateSpan([10, 4, 5, 90, 120, 80]))