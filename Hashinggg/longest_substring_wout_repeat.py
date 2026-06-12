def longest_substring_without_repeating_characters(s):
    n= len(s)
    left=0
    maxlen=0
    charset=set()
    for right in range(n):
        while (s[right] in charset):
            charset.remove(s[left])
            left= left+1
        maxlen= max(maxlen, right-left+1)
        charset.add(s[right])
    return maxlen

print(longest_substring_without_repeating_characters("abcabcbb"))