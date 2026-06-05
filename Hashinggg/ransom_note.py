def ransom_note(ransomnote, magazine):
    seen={}
    for char in magazine:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    for char in ransomnote:
        if char in seen:
            seen[char]-=1
            if seen[char]==0:
                del seen[char]
        else:
            return False
    return True

print(ransom_note("aa", "ab"))
        