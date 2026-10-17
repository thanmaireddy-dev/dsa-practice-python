#nums=[4,8,5,2,25]
#result=[2,5,2,-1,-1]
def next_smaller(nums):
    n=len(nums)
    stack=[]
    result=[0]*n
    for i in range(n-1,-1,-1):
        while stack and stack[-1]>=nums[i]:
            stack.pop()
        if not stack:
            result[i]= -1
        elif stack[-1]<nums[i]:
            result[i]= stack[-1]
        stack.append(nums[i])
    return result

print(next_smaller([4,8,5,2,25]))

    