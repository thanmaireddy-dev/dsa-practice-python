def search_in_rotated_sorted_array_II(nums, target):
    n=len(nums)
    low=0
    high=n-1
    while (low<=high):
        mid=(low+high)//2
        if nums[low]==nums[mid]==nums[high]:
            low=low+1
            high=high-1
            continue
        if nums[mid]==target:
            return True
        elif nums[low]<=nums[mid]:
            if nums[low]<=target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<target<nums[high]:
                low=mid+1
            else:
                high=mid-1
    return False

print(search_in_rotated_sorted_array_II([2,5,6,0,0,1,2],0))