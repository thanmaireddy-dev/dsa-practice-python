def word_pattern(s, pattern):
    seen={}
    check= set()
    word_list= s.split()
    if len(word_list)!= len(pattern):
        return False
    
    for char, word in zip(pattern, s.split()):
        if char not in seen:
            if word not in check:
                seen[char]= word
                check.add(word)
            else:
                return False
        else:
            if seen[char]==word:
                pass
            else:
                return False
    return True

print(word_pattern("dog cat dog dog", "aaaa"))
        
        
        