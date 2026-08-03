class Solution(object):
    def evalRPN(self, tokens):
        stack=[]
        operators={'*','-', '/', '+'}
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else:
                op2=stack.pop()
                op1=stack.pop()
                if char=='*':
                    result= op1*op2
                elif char=='+':
                    result= op1+op2
                elif char=='/':
                    result= int(float(op1)/op2)
                elif char=='-':
                    result= op1-op2
                stack.append(result)
        return stack.pop()