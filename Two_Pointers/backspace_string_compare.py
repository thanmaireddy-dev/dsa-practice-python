def backspaceCompare(s, t):
    p1 = len(s) - 1
    p2 = len(t) - 1
    while p1 >= 0 or p2 >= 0:
        s_backspace = 0
        while p1 >= 0:
            if s[p1] == '#':
                s_backspace += 1
                p1 -= 1
            elif s_backspace > 0:
                s_backspace -= 1
                p1 -= 1
            else:
                break
        t_backspace = 0
        while p2 >= 0:
            if t[p2] == '#':
                t_backspace += 1
                p2 -= 1
            elif t_backspace > 0:
                t_backspace -= 1
                p2 -= 1
            else:
                break
        if p1 >= 0 and p2 >= 0:
            if s[p1] != t[p2]:
                return False
        elif (p1 >= 0) != (p2 >= 0):
            return False
        p1 -= 1
        p2 -= 1
    return True

print(backspaceCompare("ab#c", "ad#c"))
