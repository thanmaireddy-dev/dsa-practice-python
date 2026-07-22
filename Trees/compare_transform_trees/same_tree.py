class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p and q and (p.val!=q.val):
            return False
        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)