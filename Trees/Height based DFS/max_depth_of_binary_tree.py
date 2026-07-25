from collections import deque
class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        queue= deque()
        queue.append(root)
        count=0
        while queue:
            n=len(queue)
            for i in range(n):
                root=queue.popleft()
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            count= count+1
        return count