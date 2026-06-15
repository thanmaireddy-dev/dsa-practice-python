def sort_characters_by_frequency(s):
    seen={}
    result=[]
    freq_pairs=[]
    for char in s:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    for kar in seen:
        freq= seen[kar]
        pair= [freq, kar]
        freq_pairs.append(pair)
    freq_pairs.sort()
    n= len(freq_pairs)
    
    for charrr in reversed(freq_pairs[-n:]):
        result.append(charrr[1]* charrr[0])
        strr= "".join(result)
    return strr

print(sort_characters_by_frequency("tree"))