def hasCycle(head):
    if head is None:
        return False
    double=single=head
    while double is not None and double.next is not None:
        double= double.next.next
        single= single.next
        if single==double:
            return True
    return False