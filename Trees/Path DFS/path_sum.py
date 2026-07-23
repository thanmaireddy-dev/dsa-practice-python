class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        stack=[(root, root.val)]
        while stack:
            root,currsum= stack.pop()
            if root.left is None and root.right is None:
                if currsum==targetSum:
                    return True
            if root.right:
                stack.append((root.right, currsum+ root.right.val))
            if root.left:
                stack.append((root.left, currsum+ root.left.val))
        return False