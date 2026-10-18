def nextGreaterElements(nums):
    n= len(nums)
    result=[0]*n
    stack=[]
    for i in range(2*n-1, -1,-1):
        while stack and stack[-1]<=nums[i%n]:
            stack.pop()
        if not stack:
            result[i%n]=-1
        elif stack[-1]>nums[i%n]:
            result[i%n]= stack[-1]
        stack.append(nums[i%n])
    return result

print(nextGreaterElements([1,2,3,4,3]))