def group_anagrams(strs):
    seen={}
    for word in strs:
        sorted_word= "".join(sorted(word))
        if sorted_word in seen:
            seen[sorted_word].append(word)
        else:
            seen[sorted_word]= [word]
    return list(seen.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))