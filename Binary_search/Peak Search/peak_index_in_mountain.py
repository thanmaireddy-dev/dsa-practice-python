def peak_index_in_mountain_array(nums):
    n=len(nums)
    low=0
    high=n-1
    while (low<high):
        mid=(low+high)//2
        if nums[mid]>nums[mid+1]:
            res=mid
            high=mid
        else:
            low=mid+1
    return res

print(peak_index_in_mountain_array([0,2,1,0]))
    