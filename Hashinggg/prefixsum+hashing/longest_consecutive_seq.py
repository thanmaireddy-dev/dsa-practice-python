def longest_consecutive_sequence(nums):
    numset= set(nums)
    streak=0
    maxstreak=0
    for num in numset:
        if num-1 not in numset:
            currnum= num
            streak=1
            while currnum+1 in numset:
                currnum= currnum+1
                streak= streak+1
            maxstreak= max(maxstreak, streak)
    return maxstreak

print(longest_consecutive_sequence([0,3,7,2,5,8,4,6,0,1]))
    
    