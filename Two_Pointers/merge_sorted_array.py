def merge_sorted_array(nums1, m, nums2, n):
    p1= m-1
    p2= n-1
    tobereplaced= len(nums1)-1
    while (p1>=0) and (p2>=0):
        if nums1[p1]> nums2[p2]:
            nums1[tobereplaced]= nums1[p1]
            p1=p1-1
            tobereplaced-=1
        else:
            nums1[tobereplaced]= nums2[p2]
            p2=p2-1
            tobereplaced-=1
    while (p2>=0):
        nums1[tobereplaced]= nums2[p2]
        p2=p2-1
        tobereplaced-=1
    
    return nums1

print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))