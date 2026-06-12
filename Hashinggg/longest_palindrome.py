def longest_palindrome(s):
    seen={}
    ans=0
    has_odd= False
    for char in s:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    for val in seen.values():
        if val%2==0:
            ans= ans+ val
        else:
            ans= ans+ (val-1)
            has_odd= True
    if has_odd==True:
        ans= ans+1
    return ans

print(longest_palindrome("ccc"))