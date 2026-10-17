def nextGreaterElement(nums1, nums2):
    n= len(nums2)
    m= len(nums1)
    stack=[]
    result=[0]*m
    seen={}
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<=nums2[i]:
            stack.pop()
        if not stack:
            seen[nums2[i]]=-1
        elif stack[-1]>nums2[i]:
            seen[nums2[i]]=stack[-1]
        stack.append(nums2[i])
    for i in range(m):
        result[i]=seen[nums1[i]]
    return result

print(nextGreaterElement([2,4],[1,2,3,4]))