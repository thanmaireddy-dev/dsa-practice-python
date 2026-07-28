class Solution(object):
    def diameterOfBinaryTree(self, root):
        max_diameter= [0]
        def height(root):
            if root is None:
                return 0
            leftheight= height(root.left)
            rightheight= height(root.right)
            diameter= leftheight+ rightheight
            max_diameter[0]= max(max_diameter[0], diameter)

            return 1+ max(leftheight, rightheight)
        height(root)
        return max_diameter[0]