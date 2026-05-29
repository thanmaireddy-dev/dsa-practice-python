def minimum_element_after_replacement_with_digit_sum(nums):
    result=[]
    for num in nums:
        digit= sum(map(int, str(num)))
        result.append(digit)
    return min(result)

print(minimum_element_after_replacement_with_digit_sum([10,12,13,14]))
    