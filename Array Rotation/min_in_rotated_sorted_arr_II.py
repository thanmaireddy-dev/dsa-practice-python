def findMin(nums):
    n= len(nums)
    low=0
    high=n-1
    while (low<=high):
        mid=(low+high)//2
        if nums[mid]==nums[high]:
            high=high-1
        elif nums[mid]> nums[high]:
            low=mid+1
        else:
            high=mid
    return nums[low]
print(findMin([2,2,2,2,0,1,1]))