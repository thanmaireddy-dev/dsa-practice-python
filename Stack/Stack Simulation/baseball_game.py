class Solution(object):
    def calPoints(self, ops):
        stack=[]
        for char in ops:
            try:
                stack.append(int(char))
            except ValueError:
                if char=='+':
                    stack.append(stack[-1]+ stack[-2])
                elif char=='C':
                    stack.pop()
                else:
                    stack.append(stack[-1]*2) 
        return sum(stack)