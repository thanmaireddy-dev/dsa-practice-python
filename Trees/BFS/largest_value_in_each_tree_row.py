from collections import deque
def largestValues(self, root):
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
        result.append(max(level))
    return result