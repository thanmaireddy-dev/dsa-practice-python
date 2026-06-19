def binary_search(nums, target):
    n= len(nums)
    low=0
    high=n-1
    while (low<=high):
        mid= (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low= mid+1
        else:
            high= mid-1
    return -1

print(binary_search([-1,0,3,5,9,12],9))