def rotateRight(head, k):
    if not head:
        return head
    length=1
    tail=head
    while tail.next is not None:
        length+=1
        tail=tail.next
    k=k%length
    if k==0:
        return head
    current=head
    for i in range(length-k-1):
        current= current.next
    new_head= current.next
    current.next=None
    tail.next= head
    return new_head