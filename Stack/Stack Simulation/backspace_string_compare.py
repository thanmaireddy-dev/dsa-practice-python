class Solution(object):
    def backspaceCompare(self, s, t):
        stack1=[]
        stack2=[]
        for char1 in s:
            if stack1:
                if char1!='#':
                    stack1.append(char1)
                else:
                    stack1.pop()
            else:
                if char1!='#':
                    stack1.append(char1)
                else:
                    pass
                
        for char2 in t:
            if stack2:
                if char2!='#':
                    stack2.append(char2)
                else:
                    stack2.pop()
            else:
                if char2!='#':
                    stack2.append(char2)
                else:
                    pass

        ans1=""
        ans2=""
        for c in stack1:
            ans1= ans1+c
        for d in stack2:
            ans2= ans2+d
        return ans1==ans2