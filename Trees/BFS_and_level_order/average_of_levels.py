class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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

print(averageOfLevels([3,9,20,null,null,15,7]))