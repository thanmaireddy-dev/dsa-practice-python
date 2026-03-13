def longest_substring_with_atmost_k_distinct_characters(s,k):
    n= len(s)
    p1=p2=0
    maxlen=0
    charset= {}
    for p1 in range(n):
        if s[p1] in charset:
            charset[s[p1]]+=1
        else:
            charset[s[p1]]=1
            
        while len(charset)>2:
            charset[s[p2]]-=1
            if charset[s[p2]]==0:
                del charset[s[p2]]
            p2= p2+1
        maxlen= max(maxlen, p1-p2+1)
        
    return maxlen

print(longest_substring_with_atmost_k_distinct_characters("abeddefg", 3))
    