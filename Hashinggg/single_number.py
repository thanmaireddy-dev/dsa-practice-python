def single_number(nums):
    seen={}
    for num in nums:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1
    
    for key,val in seen.items():
        if val==1:
            return key
        
print(single_number([4,1,2,1,2]))