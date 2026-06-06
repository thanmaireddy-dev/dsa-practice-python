def intersection_of_two_arrays(nums1, nums2):
    set1= set(nums1)
    set2= set(nums2)
    result= set1 & set2
    return list(result)

print(intersection_of_two_arrays([2,2,3], [1,2,3,4,5]))