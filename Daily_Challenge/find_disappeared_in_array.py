def disappeared_numbers(nums):
    for num in nums:
        i= abs(num)-1
        nums[i]= -1*abs(nums[i])
    result=[]
    for i,num in enumerate(nums):
        if num>0:
            result.append(i+1)
    return result

print(disappeared_numbers([4,3,2,7,8,2,3,1]))
        
    