def peak_index_in_mountain_array(nums):
    n= len(nums)
    low=1
    high=n-2 #cuz the peak element can never be the first or last element!!
    while (low<=high):
        mid=(low+high)//2
        if nums[mid]> nums[mid-1] and nums[mid]> nums[mid+1]:
            return mid
        elif nums[mid]< nums[mid-1]:
            high=mid-1
        elif nums[mid]< nums[mid+1]:
            low=mid+1

print(peak_index_in_mountain_array([3, 9, 8, 6, 4]))
    