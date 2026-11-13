def swapPairs(head):
    dummy= ListNode('D')
    dummy.next=head
    prev=dummy
    while prev.next is not None and prev.next.next is not None:
        swap1= prev.next
        swap2= prev.next.next
        swap1.next= swap2.next
        swap2.next= swap1
        prev.next= swap2
        prev= swap1
    return dummy.next