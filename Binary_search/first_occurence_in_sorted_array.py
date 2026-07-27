def first_occurence(nums,target):
    n=len(nums)
    low=0
    high= n-1
    result=-1
    while (low<=high):
        mid= (low+high)//2
        if nums[mid]==target:
            result=mid
            high=mid-1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return result 

print(first_occurence([1,2,2,2,3,4,5],2))
    