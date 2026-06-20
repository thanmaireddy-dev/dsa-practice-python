def  find_first_and_last_position_of_an_element_in_sorted_array(nums, target):
    n=len(nums)
    def find_first(nums, target):
        first= -1
        low=0
        high=n-1
        while (low<=high):
            mid= (low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first
    
    def find_last(nums, target):
        last=-1
        low=0
        high=n-1
        while (low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last
    
    return [find_first(nums,target), find_last(nums, target)]

print(find_first_and_last_position_of_an_element_in_sorted_array([5,7,7,8,8,10],8))
                
            
                    
            
    