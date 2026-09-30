def check_if_array_is_rotated_and_sorted(nums):
    n=len(nums)
    count=0
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            count=count+1
    if nums[n-1]>nums[0]:
        count=count+1
    if count>1:
        return False
    return True

print(check_if_array_is_rotated_and_sorted([2,1,3,4]))