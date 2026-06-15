def top_k_frequent_elements(nums,k):
    seen={}
    freq_pairs=[]
    result=[]
    for num in nums:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1
    for number in seen:
        freq= seen[number]
        pair= [number, seen]
        freq_pairs.append(pair)
    freq_pairs.sort()
    
    for num in reversed(freq_pairs[-k:]):
        result.append(num[1])
    return result

print(top_k_frequent_elements([1,1,1,2,2,3], 2))
        
        
    