def count_occurences_in_sorted_array_GFG(nums, target):
    n= len(nums)
    def find_first(nums, target):
        low=0
        high=n-1
        first=-1
        while (low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return first
    def find_last(nums, target):
        low=0
        high=n-1
        last=-1
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
    
    res1=find_first(nums, target)
    res2=find_last(nums, target)
    if res1==-1:
        return 0
    return res2-res1+1

print(count_occurences_in_sorted_array_GFG([1,1,2,2,2,2,3,4],1))
        
                
    