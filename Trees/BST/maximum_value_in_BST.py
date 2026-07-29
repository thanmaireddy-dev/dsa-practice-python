def maximum_value(root):
    if root is None:
        return None
    while root.right:
        root= root.right
    return root.val