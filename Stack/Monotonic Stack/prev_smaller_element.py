def prev_smaller(nums):
    n= len(nums)
    stack=[]
    result=[0]*n
    for i in range(n):
        while stack and stack[-1]>=nums[i]:
            stack.pop()
        if not stack:
            result[i]= -1
        elif stack[-1]<nums[i]:
            result[i]= stack[-1]
        stack.append(nums[i])
    return result

print(prev_smaller([1,6,2]))
    