def contains_duplicate_II(nums,k):
    seen={}
    for i,num in enumerate(nums):
        if num in seen and abs(seen[num]-i)<=k:
            return True
        seen[num]=i
    return False

print(contains_duplicate_II([1,2,3,1],3))