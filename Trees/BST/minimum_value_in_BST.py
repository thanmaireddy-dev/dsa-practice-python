def minimum_value(root):
    if root is None:
        return None
    while root.left:
        root= root.left
    return root.val