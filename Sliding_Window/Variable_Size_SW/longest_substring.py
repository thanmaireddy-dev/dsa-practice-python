def longest_substring_without_repeating_characters(s):
    n= len(s)
    maxlen=0
    left=0
    charset= set()
    for right in range(n):
        while s[right] in charset:
            charset.remove(s[left])
            left= left+1
        charset.add(s[right])
        maxlen= max(maxlen, len(charset))
        
    return maxlen

print(longest_substring_without_repeating_characters("pwwkew"))
        