#same as lc HARD 410- split array largest sum
def split_array_largest_sum(nums,k):
    def can_split(mid, nums,k):
        total_sum=0
        partitions=1
        for num in nums:
            total_sum= total_sum+num
            if total_sum>mid:
                partitions+=1
                total_sum=num
        if partitions<=k:
            return True
        else:
            return False
        
    low=max(nums)
    high=sum(nums)
    while low<=high:
        mid=(low+high)//2
        if can_split(mid, nums, k):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(split_array_largest_sum([1,2,3,4,5],2))
