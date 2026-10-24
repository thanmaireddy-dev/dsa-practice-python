def removeKdigits(num, k):
    stack=[]
    count=0
    for char in num:
        while stack and count<k and stack[-1]>int(char):
            stack.pop()
            count=count+1
        stack.append(int(char))
    while (stack and count<k):
        stack.pop()
        count=count+1
    if not stack:
        return '0'
    return str(int("".join(map(str,stack))))

print(removeKdigits("1432219",3))