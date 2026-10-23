def largestRectangleArea(nums):
    n=len(nums)
    nextsmaller=[0]*n
    prevsmaller=[0]*n
    stack1=[]
    stack2=[]
    maxarea=0
    for i in range(n-1,-1,-1):
        while stack1 and nums[stack1[-1]]>=nums[i]:
            stack1.pop()
        if not stack1:
            nextsmaller[i]=n
        else:
            nextsmaller[i]=stack1[-1]
        stack1.append(i)
    for i in range(n):
        while stack2 and nums[stack2[-1]]>=nums[i]:
            stack2.pop()
        if not stack2:
            prevsmaller[i]=-1
        else:
            prevsmaller[i]=stack2[-1]
        stack2.append(i)
    for i in range(n):
        height= nums[i]
        width= nextsmaller[i]-prevsmaller[i]-1
        area=height*width
        maxarea= max(maxarea, area)
    return maxarea

print(largestRectangleArea([2,1,5,6,2,3]))