def isomorphic_strings(s,t):
    seen={}
    check= set()
    for char_s, char_t in zip(s,t):
        if char_s in seen:
            if seen[char_s]== char_t:
                pass
            else:
                return False
        else:
            if char_t in check:
                return False
            else:
                seen[char_s]= char_t
                check.add(char_t)
    return True
                
print(isomorphic_strings("eggnogg", "addesdd"))