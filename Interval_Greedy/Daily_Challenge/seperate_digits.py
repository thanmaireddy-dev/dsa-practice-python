#LC 2553
def seperate_digits_in_an_array(nums):
    result=[]
    for num in nums:
        digit= list(map(int, str(num)))
        result.extend(digit)
    return result
    
    
print(seperate_digits_in_an_array([2344,5600]))