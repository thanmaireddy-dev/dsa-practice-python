def cycle(head):
    visited= set()
    current=head
    while current is not None:
        if current in visited:
            return True
        visited.add(current)
        current=current.next
    return False