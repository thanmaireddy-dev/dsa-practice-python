def intersection_of_multiple_arrays(nums):
    n= len(nums)
    running_set= set(nums[0])
    for i in range(1,n):
        result= running_set & set(nums[i])
        running_set= result
    return sorted(list(result))

print(intersection_of_multiple_arrays([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))