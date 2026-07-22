class Solution(object):
    def isSymmetric(self, root):
        def dfs(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left and right and (left.val!=right.val):
                return False
            return dfs(left.left,right.right) and dfs(left.right, right.left)
        return dfs(root.left,root.right)