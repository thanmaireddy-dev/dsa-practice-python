def find_the_difference(s,t):
    seen={}
    for char in s:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    for letter in t:
        if letter in seen and seen[letter]>0:
            seen[letter]-=1
        else:
            return letter
        
print(find_the_difference("abcd", "abcde"))