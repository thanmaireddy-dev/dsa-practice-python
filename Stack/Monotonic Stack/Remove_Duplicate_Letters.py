def removeDuplicateLetters(s):
    n= len(s)
    stack=[]
    visited=set()
    seen={}
    for i in range(n):
        seen[s[i]]=i
    for i,char in enumerate(s):
        if char in visited:
            continue
        while stack and stack[-1]>char and seen[stack[-1]]>i:
            visited.remove(stack[-1])
            stack.pop()
        stack.append(char)
        visited.add(char)
    return "".join(stack)

print(removeDuplicateLetters("bcabc"))