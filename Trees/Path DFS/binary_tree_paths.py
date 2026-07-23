class Solution(object):
    def binaryTreePaths(self, root):
        if root is None:
            return []
        stack=[(root, str(root.val))]
        result=[]
        while stack:
            root,path= stack.pop()
            if root.left is None and root.right is None:
                result.append(path)
            if root.right:
                stack.append((root.right, path+ "->" + str(root.right.val)))
            if root.left:
                stack.append((root.left, path+ "->" + str(root.left.val)))
        return result