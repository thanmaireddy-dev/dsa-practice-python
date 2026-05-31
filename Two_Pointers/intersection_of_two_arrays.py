def intersection_of_two_arrays(nums1, nums2):
    n= len(nums1)
    m= len(nums2)
    nums1.sort()
    nums2.sort()
    result= set()
    p1=p2=0
    while (p1<n and p2<m):
        if nums1[p1]< nums2[p2]:
            p1=p1+1
        elif nums1[p1]> nums2[p2]:
            p2=p2+1
        else:
            result.add(nums1[p1])
            p1=p1+1
            p2=p2+1
    return list(result)
        
print(intersection_of_two_arrays([1,2,2,1],[2,2]))

"""
can also be done with set intersection method.
set1= set(nums1)
set2=set(nums2)
result= set1 & set2 
return list(result)
"""
