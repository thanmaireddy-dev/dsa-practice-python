class Solution(object):
    def isValid(self, s):
        seen={
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack =[]
        for char in s:
            if char not in seen:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1]==seen[char]:
                        stack.pop()
                    else:
                        return False
        return not stack