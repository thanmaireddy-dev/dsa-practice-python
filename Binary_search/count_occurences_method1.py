import bisect
def count_occurences_in_sorted_array_GFG(nums,target):
    #method 1
    index1= bisect.bisect_left(nums, target)
    index2= bisect.bisect_right(nums, target)
    return (index2-index1)

print(count_occurences_in_sorted_array_GFG([1 ,1, 2, 2, 2, 2, 3], 3))