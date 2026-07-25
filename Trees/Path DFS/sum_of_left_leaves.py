class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        queue= deque()
        queue.append(root)
        totalsum=0
        while queue:
            root= queue.popleft()
            if root.left:
                if root.left.left is None and root.left.right is None:
                    totalsum= totalsum+ root.left.val
                else:
                    queue.append(root.left)
            if root.right:
                queue.append(root.right)
        return totalsum