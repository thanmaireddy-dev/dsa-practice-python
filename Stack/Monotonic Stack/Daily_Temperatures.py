def dailyTemperatures(nums):
    n= len(nums)
    result=[0]*n
    stack=[]
    for i in range(n-1,-1,-1):
        while stack and nums[stack[-1]]<=nums[i]:
            stack.pop()
        if not stack:
            result[i]=0
        elif nums[stack[-1]]>nums[i]:
            result[i]= stack[-1]-i
        stack.append(i)
    return result

print(dailyTemperatures([73,74,75,71,69,72,76,73]))