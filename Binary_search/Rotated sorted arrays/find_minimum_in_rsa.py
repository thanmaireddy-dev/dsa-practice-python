def find_minimum_in_rotated_sorted_array(nums):
    n=len(nums)
    low=0
    high=n-1
    while (low<high):
        mid=(low+high)//2
        if nums[mid]> nums[high]:
            low=mid+1
        else:
            high=mid-1
    return nums[low]

print(find_minimum_in_rotated_sorted_array([11,13,15,17]))
        