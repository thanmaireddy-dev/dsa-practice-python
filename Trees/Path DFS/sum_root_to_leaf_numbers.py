class Solution(object):
    def sumNumbers(self, root):
        if root is None:
            return 0
        stack=[(root, root.val)]
        totalsum=0
        while stack:
            root, pathsum= stack.pop()
            if root.left is None and root.right is None:
                totalsum= totalsum+ pathsum
            if root.right:
                stack.append((root.right, int(str(pathsum)+ str(root.right.val))))
            if root.left:
                stack.append((root.left, int(str(pathsum)+ str(root.left.val))))
        return totalsum
    
            