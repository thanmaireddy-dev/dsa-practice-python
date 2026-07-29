class Solution(object):
    def kthSmallest(self, root, k):
        result=[]
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result[k-1]