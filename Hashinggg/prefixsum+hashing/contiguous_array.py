def contiguous_array(nums):
    n= len(nums)
    seen={0:-1}
    prefixsum=0
    maxlen=0
    for i, num in enumerate(nums):
        if num==0:
            num= -1
        prefixsum= prefixsum+ num
        if prefixsum in seen:
            length= i- seen[prefixsum]
            maxlen= max(maxlen, length)
        else:
            seen[prefixsum]=i
    return maxlen

print(contiguous_array([0,1,1,1,1,1,0,0,0]))