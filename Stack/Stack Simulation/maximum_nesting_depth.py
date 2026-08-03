class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        maxdepth=0
        depth=0
        for char in s:
            if char=='(':
                stack.append(char)
                depth= len(stack)
                maxdepth= max(depth, maxdepth)
            elif char==')':
                    stack.pop()
        return maxdepth