def reverse_linked_list(head):
    current=head
    prev=None
    while current is not None:
        next_node=current.next
        current.next=prev
        prev=current
        current=next_node
    head=prev
    return head
