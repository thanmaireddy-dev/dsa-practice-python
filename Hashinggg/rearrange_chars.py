def rearrange_characters_to_make_target_string(s,target):
    smap={}
    targetmap={}
    minchar= float('inf')
    for char in target:
        if char in targetmap:
            targetmap[char]+=1
        else:
            targetmap[char]=1
    for char in s:
        if char in smap:
            smap[char]+=1
        else:
            smap[char]=1
    
    for uniquechar in targetmap:
        if uniquechar in smap:
            availablechars= smap[uniquechar]
        else:
            return 0
        
        charcount= availablechars//targetmap[uniquechar]
        minchar= min(minchar, charcount)
    return minchar

print(rearrange_characters_to_make_target_string("abbaccaddaeea", "aaaaa"))
