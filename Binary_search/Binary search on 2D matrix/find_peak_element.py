def find_peak_element(nums):
    n=len(nums)
    low=0
    high=n-1
    while (low<high):
        mid= (low+high)//2
        if nums[mid]>nums[mid+1]:
            high=mid
        else:
            low=mid+1
    return low

print(find_peak_element([1,3,2,8,4,3]))