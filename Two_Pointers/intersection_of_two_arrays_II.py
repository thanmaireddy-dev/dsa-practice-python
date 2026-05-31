def intersection_of_two_arrays_II(nums1, nums2):
    n= len(nums1)
    m= len(nums2)
    nums1.sort()
    nums2.sort()
    result= []
    p1=p2=0
    while (p1<n and p2<m):
        if nums1[p1]< nums2[p2]:
            p1=p1+1
        elif nums1[p1]> nums2[p2]:
            p2=p2+1
        else:
            result.append(nums1[p1])
            p1=p1+1
            p2=p2+1
    return result

print(intersection_of_two_arrays_II([1,2,2,1], [2,2]))