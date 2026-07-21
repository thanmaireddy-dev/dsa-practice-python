from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        if root is None:
            return []
        queue= deque()
        queue.append(root)
        result=[]

        while queue:
            summ=0
            n=len(queue)
            for i in range(n):
                root= queue.popleft()
                summ= summ+root.val
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.append(float(summ)/n)
        return result