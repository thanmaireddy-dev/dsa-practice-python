class Solution(object):
    def maxPathSum(self, root):
        result=[root.val]
        def dfs(root):
            if root is None:
                return 0
            leftmax= dfs(root.left)
            rightmax= dfs(root.right)
            leftmax= max(0, leftmax)
            rightmax= max(0,rightmax)
            
            result[0]= max(result[0], root.val+leftmax+rightmax)
            return root.val+ max(leftmax, rightmax)
        dfs(root)
        return result[0]