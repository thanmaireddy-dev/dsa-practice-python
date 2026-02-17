def assign_cookies(g,s):
    g.sort()
    s.sort()
    p1=p2=0
    count=0
    while p1< len(g) and p2<len(s):
        if s[p2]>=g[p1]:
            count= count+1
            p1+=1
            p2+=1
        else:
            p2+=1
    return count

print(assign_cookies([1,2,3], [1,1]))