def reverse_a_string(s):
    n= len(s)
    p1=0
    p2= n-1
    while (p1<p2):
        s[p1], s[p2]= s[p2], s[p1]
        p1= p1+1
        p2= p2-1
    return s

print(reverse_a_string(["h", "e", "l", "l", "o"]))