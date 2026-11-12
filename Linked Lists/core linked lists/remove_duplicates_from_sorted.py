class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    dummy= ListNode('D')
    dummy.next=head
    prev=dummy
    current=head
    while current is not None:
        if current.val==prev.val:
            prev.next=current.next
        else:
            prev=current
        current=current.next
    return dummy.next