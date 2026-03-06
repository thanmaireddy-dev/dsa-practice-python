def find_all_anagrams_in_a_string(s,p):
    n= len(s)
    k= len(p)
    p_freq= {}
    window_freq= {}
    result=[]
    
    if n<k:
        return []
    
    for char in p:
        if char in p_freq:
            p_freq[char]+=1
        else:
            p_freq[char]=1
            
    for i in range(k):
        char= s[i]
        if char in window_freq:
            window_freq[char]+=1
        else:
            window_freq[char]=1
            
    if p_freq== window_freq:
        result.append(0)
    
    for i in range(k,n):
        newchar= s[i]
        oldchar= s[i-k]
        if newchar in window_freq:
            window_freq[newchar]+=1
        else:
            window_freq[newchar]=1
        window_freq[oldchar]-=1
        
        if window_freq[oldchar]==0:
            del window_freq[oldchar]
        
        if  window_freq== p_freq:
            result.append(i-k+1)
            
    return result 

print(find_all_anagrams_in_a_string("abab", "ab"))
            
    
    
    
    