def reverse_degree_of_string(s):
    summ=0
    n= len(s)
    for i in range(n):
        summ= summ+ (i+1)*(27-(ord(s[i])-96))
    return summ

print(reverse_degree_of_string("abc"))
