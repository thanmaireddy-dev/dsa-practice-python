def search_in_rotated_sorted_array(nums, target):
    n= len(nums)
    low=0
    high=n-1
    while (low<=high):
        mid= (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[low]<=nums[mid]:
            if nums[low]<=target<nums[high]:
                high=mid-1
            else:
                low=mid+1
        else:
            if nums[mid]<target<=nums[high]:
                low=mid+1
            else:
                high=mid-1
    return -1

print(search_in_rotated_sorted_array([4,5,6,7,0,1,2],0))
                
            
    
        
    