from collections import deque
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        queue= deque()
        queue.append(root)
        result=[]

        while queue:
            n=len(queue)
            level=[]
            for i in range(n):
                root= queue.popleft()
                level.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.append(level[-1])
        return result