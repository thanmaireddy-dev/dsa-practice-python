def partition(head, x):
    if head is None or head.next is None:
        return head
    left=ListNode()
    right= ListNode()
    ltail, rtail= left, right
    while head is not None:
        if head.val<x:
            ltail.next= head
            ltail= ltail.next
        else:
            rtail.next= head
            rtail= rtail.next
        head= head.next
    rtail.next= None
    ltail.next= right.next
    return left.next
    