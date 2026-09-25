def find_duplicates(nums):
    result=[]
    for num in nums:
        i= abs(num)-1
        if nums[i]<0:
            result.append(i+1)
        else:
            nums[i]= -1* abs(nums[i])
    return result

print(find_duplicates([4,3,2,7,8,2,3,1]))
            
    