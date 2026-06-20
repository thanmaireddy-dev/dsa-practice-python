def search_insert_position(nums, target):
    n= len(nums)
    low=0
    high=n-1
    while (low<=high):
        mid= (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high= mid-1
    return low

print(search_insert_position([1,3,5,6],5))