def find_the_smallest_divisor_given_a_threshold(nums,threshold):
    def can_do(mid,nums,threshold):
        summ=0
        for num in nums:
            summ=summ+ (num+mid-1)/mid
        if summ<=threshold:
            return True
        else:
            return False
        
    low=1
    high=max(nums)
    result=high
    while (low<=high):
        mid=(low+high)//2
        if can_do(mid, nums, threshold):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(find_the_smallest_divisor_given_a_threshold([44,22,33,11,1],5))
        