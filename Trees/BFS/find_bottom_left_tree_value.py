from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        if root is None:
            return []
        queue= deque()
        queue.append(root)

        while queue:
            n=len(queue)
            answer=0
            for i in range(n):
                root= queue.popleft()
                if i==0:
                    answer=root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            
        return answer