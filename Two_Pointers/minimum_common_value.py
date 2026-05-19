def minimum_common_value(nums1, nums2):
    n= len(nums1)
    m= len(nums2)
    p1=0
    p2=0
    while (p1<n and p2<m):
        if nums1[p1]< nums2[p2]:
            p1=p1+1
        elif nums1[p1]> nums2[p2]:
            p2=p2-1
        else:
            return nums1[p1]
        
    return -1

print(minimum_common_value([1,2,3,6],[2,3,4,5]))
        
        