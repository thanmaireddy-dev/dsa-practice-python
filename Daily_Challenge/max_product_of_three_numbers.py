def maximumProduct(nums):
    n=len(nums)
    first=second=third= float('-inf')
    min1=min2= float('inf')
    for num in nums:
        if num>first:
            third=second
            second=first
            first=num
        elif num>second:
            third=second
            second=num
        elif num>third:
            third=num
        if num<min1:
            min2=min1
            min1=num
        elif num<min2:
            min2=num
    return max(first*second*third, first*min1*min2)

print(maximumProduct([-1,-2,-3,40,3,2,5]))

"""
orrr, we can just do
nums.sort()
return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])

"""