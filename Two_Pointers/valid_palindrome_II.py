def valid_palindrome_two(s):
    n= len(s)
    p1=0
    p2=n-1
    
    def is_palindrome(s, p1, p2): #helper funtion to determine if palindrome or not
        while (p1<p2):
            if s[p1]==s[p2]:
                p1=p1+1
                p2=p2-1 
            else:
                return False
        return True
    
    while(p1<p2):
        if s[p1]==s[p2]:
            p1=p1+1
            p2=p2-1
        else:
            return is_palindrome(s,p1+1,p2) or is_palindrome(s,p1,p2-1)
    return True


print(valid_palindrome_two("ablmbkd"))
                