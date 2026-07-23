class Solution(object):
    def isSubtree(self, root, subRoot):
        def isIdentical(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is None:
                return False
            if root and subRoot and (root.val!=subRoot.val):
                return False
            return isIdentical(root.left, subRoot.left) and isIdentical(subRoot.right, root.right)
            

        stack=[]
        stack.append(root)
        while stack:
            root= stack.pop()
            if root.val==subRoot.val:
                if isIdentical(root, subRoot):
                    return True
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        return False