def maxVowels(s, k):
    n= len(s)
    vowels=0
    seen={'a','e','i','o','u'}
    for i in range(k):
        if s[i] in seen:
            vowels= vowels+1
    maxvowels= vowels
    for right in range(k,n):
        if s[right] in seen:
            vowels+=1
        if s[right-k] in seen:
            vowels-=1
        maxvowels= max(maxvowels, vowels)
    return maxvowels

print(maxVowels("wedowhatweeio",5))