def single_number(nums):
    result=0
    for num in nums:
        result= result^num
    return result

print(single_number([4,1,2,1,2]))
#CAN ALSO BE SOLVED USING DICTIONARY TC- O(n) and SC: O(n)