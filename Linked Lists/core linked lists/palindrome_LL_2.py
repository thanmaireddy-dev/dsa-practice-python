def palindrome_LL_2(head):
    if not head or not head.next:
        return True
    fast=slow=head
    while fast is not None and fast.next is not None:
        fast= fast.next.next
        slow= slow.next
    current=slow
    prev=None
    while current is not None:
        nextnode= current.next
        current.next=prev
        prev=current
        current= nextnode
    h1= head
    h2=prev
    while h2 is not None:
        if h1.val!=h2.val:
            return False
        else:
            h1=h1.next
            h2=h2.next
    return True