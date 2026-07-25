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

list1=[1,2,3]
lsut2= [3,4,5]
print(list1+ lsut2)