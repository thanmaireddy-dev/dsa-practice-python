def longest_repeating_character_replacement(s,k):
    n= len(s)
    maxlen=0
    maxfreq=0
    left=0
    charset={}
    for right in range(n):
        if s[right] in charset:
            charset[s[right]]+=1
        else:
            charset[s[right]]=1
        maxfreq= max(maxfreq, charset[s[right]])
        while ((right-left+1)-maxfreq)>k:
            charset[s[left]]-=1
            if charset[s[left]]==0:
                del charset[s[left]]
            left= left+1
        maxlen= max(maxlen, right-left+1)
    return maxlen

print(longest_repeating_character_replacement("ABAB", 2))
            
            
    
    