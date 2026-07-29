class Solution(object):
    def isValidBST(self, root):
        def validate(root, low, high):
            if root is None:
                return True
            if not(low< root.val< high):
                return False
            return validate(root.left, low, root.val) and validate(root.right, root.val, high)
        return validate(root, float('-inf'), float('inf'))