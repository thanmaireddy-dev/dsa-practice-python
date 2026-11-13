def oddEvenList(head):
    if head is None or head.next is None:
        return head
    odd= odd_head= head
    even= even_head= head.next
    while even is not None and even.next is not None:
        odd.next= even.next
        odd= odd.next
        even.next= odd.next
        even= even.next
    odd.next= even_head
    return odd_head