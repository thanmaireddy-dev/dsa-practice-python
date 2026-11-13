def middle_of_LL(head):
    n=0
    current=head
    while current is not None:
        n=n+1
        current=current.next
        
    current=head
    for i in range(n//2):
        current=current.next
    return current 