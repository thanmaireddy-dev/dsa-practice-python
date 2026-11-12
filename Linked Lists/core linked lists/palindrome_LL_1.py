def palindrome(head):
    vals=[]
    current=head
    while current:
        vals.append(current.val)
        current=current.next
    return vals==vals[::-1]
    