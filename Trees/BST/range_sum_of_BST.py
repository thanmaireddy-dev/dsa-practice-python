class Solution(object):
    def rangeSumBST(self, root, low, high):
        result=[]
        summ=0
        def inorder(root):
            if root is None:
                return None
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        
        for num in result:
            if low<=num<=high:
                summ= summ+num
        return summ