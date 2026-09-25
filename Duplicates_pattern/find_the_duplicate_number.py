def find_the_duplicate_number(nums):
    for num in nums:
        i= abs(num)-1
        if nums[i]<0:
            return i+1
        else:
            nums[i]= -1* abs(nums[i])
            
print(find_the_duplicate_number([3,1,3,4,2]))
print(find_the_duplicate_number([3,3,3,3]))