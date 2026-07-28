def smallestPalindrome(s):
    seen={}
    firsthalf=""
    middle=""
    for char in s:
        if char in seen:
            seen[char]+=1
        else:
            seen[char]=1
    for key,val in sorted(seen.items()):
        if val%2==0:
            firsthalf= firsthalf+ (key*(val//2))
        else:
            firsthalf= firsthalf+ (key*(val//2))
            middle= middle+key
    lasthalf= firsthalf[::-1]
    result= firsthalf+middle+lasthalf
    return result

print(smallestPalindrome("qnnq"))
    