def middle_node(head):
    if head is None:
        return None
    single=double=head
    while double is not None and double.next is not None:
        double= double.next.next
        single=single.next
    return single