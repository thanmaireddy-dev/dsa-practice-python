class Solution(object):
    def makeGood(self, s):
        stack=[]
        for char in s:
            if stack:
                if stack[-1]==char:
                    stack.append(char)
                elif stack[-1]==char.lower() or stack[-1]==char.upper():
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        ans=""
        for c in stack:
            ans= ans+c
        return ans