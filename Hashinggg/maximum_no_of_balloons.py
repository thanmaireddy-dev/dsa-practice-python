def maximum_number_of_balloons(text):
    seen={'b':0, 'a':0,'l':0,'o':0,'n':0}
    for char in text:
        if char in seen:
            seen[char]+=1
    b=seen['b']
    a=seen['a']
    l=seen['l']//2
    o=seen['o']//2
    n=seen['n']
    return min(b,a,l,o,n)

print(maximum_number_of_balloons("loonbalxballpoon"))
    