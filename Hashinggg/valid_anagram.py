def valid_anagram(s,t):
    sfreq={}
    tfreq={}
    for char in s:
        if char in sfreq:
            sfreq[char]+=1
        else:
            sfreq[char]=1
    for char in t:
        if char in tfreq:
            tfreq[char]+=1
        else:
            tfreq[char]=1
    return tfreq== sfreq

print(valid_anagram("anagram", "nagaram"))