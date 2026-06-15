def number_of_good_pairs(nums):
    seen={}
    count=0
    for num in nums:
        if num in seen:
            count= count+ seen[num]
            seen[num]+=1
        else:
            seen[num]=1
    return count

print(number_of_good_pairs([1,2,3,1,1,3]))