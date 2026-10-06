def minAddToMakeValid(s):
    stack=[]
    for char in s:
        if not stack:
            stack.append(char)
        else:
            if char=='(':
                stack.append(char)
            else:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(char)
    return len(stack)

print(minAddToMakeValid("(((()"))