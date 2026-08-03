class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        answer=""
        for char in s:
            if char=='(':
                if not stack:
                    stack.append(char)
                else:
                    stack.append(char)
                    answer= answer+char
            else:
                stack.pop()
                if stack:
                    answer= answer+char
        return answer