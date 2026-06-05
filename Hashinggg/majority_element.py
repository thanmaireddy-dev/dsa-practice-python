def majority_element(nums):
    n= len(nums)
    seen={}
    for num in nums:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1
    for key,value in seen.items():
        if value > n//2:
            ans= key
            break
    return ans

print(majority_element([2,2,1,1,1,2,2]))