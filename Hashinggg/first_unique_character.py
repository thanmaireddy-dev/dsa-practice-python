def first_unique_character_in_a_string(s):
    seen={}
    for char in s:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    for i,num in enumerate(s):
        if seen[num]==1:
            return i
    return -1

print(first_unique_character_in_a_string("loveleetcode"))
