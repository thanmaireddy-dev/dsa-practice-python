class Solution(object):
    def isBalanced(self, root):
        balanced= [True]
        def height(root):
            if root is None:
                return 0
            leftheight= height(root.left)
            rightheight= height(root.right)
            
            if abs(leftheight- rightheight)>1:
                balanced[0]=False
            return 1+max(leftheight, rightheight)
        height(root)
        return balanced[0]