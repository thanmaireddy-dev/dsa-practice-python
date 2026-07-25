class Solution(object):
    def pathSum(self, root, targetSum):
        if root is None:
            return []
        stack=[(root,root.val, [root])]
        result=[]
        while stack:
            root, currsum, path= stack.pop()
            if root.left is None and root.right is None:
                if currsum==targetSum:
                    result.append(path)
            if root.right:
                stack.append((root.right, currsum+ root.right.val, path+[root.right.val]))
            if root.left:
                stack.append((root.left, currsum+ root.left.val, path+ [root.left.val]))
        return result
    