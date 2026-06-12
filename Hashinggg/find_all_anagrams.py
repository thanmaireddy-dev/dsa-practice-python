def find_all_anagrams_in_a_string(s,p):
    n= len(s)
    k= len(p)
    sfreq={}
    pfreq={}
    result=[]
    if n<k:
        return result
    for char in p:
        if char in pfreq:
            pfreq[char]+=1
        else:
            pfreq[char]=1
    for i in range(k):
        char= s[i]
        if char in sfreq:
            sfreq[char]+=1
        else:
            sfreq[char]=1
    if pfreq== sfreq:
        result.append(0)
    
    for i in range(k,n):
        newchar= s[i]
        oldchar= s[i-k]
        if newchar in sfreq:
            sfreq[newchar]+=1
        else:
            sfreq[newchar]=1
        sfreq[oldchar]-=1
        if sfreq[oldchar]==0:
            del sfreq[oldchar]
        if sfreq==pfreq:
            result.append(i-k+1)
    return result

print(find_all_anagrams_in_a_string("abab", "ab"))
    