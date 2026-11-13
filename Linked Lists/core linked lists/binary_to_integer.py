def getDecimalValue(head):
    binary=""
    current=head
    while current is not None:
        binary= binary+ str(current.val)
        current=current.next
    decimal=0
    power=0
    for digit in reversed(binary):
        if digit=='1':
            decimal= decimal+ 2**power
        power+=1
    return decimal