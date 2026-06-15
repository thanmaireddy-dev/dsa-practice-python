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
        pair= [freq, number]
        freq_pairs.append(pair)
    freq_pairs.sort()
    
    for barbie in reversed(freq_pairs[-k:]):
        result.append(barbie[1])
    return result

print(top_k_frequent_elements([1,2,1,2,1,2,3,1,3,2], 2))
    
    
        
        
    