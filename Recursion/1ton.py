def print_nums(n):
    if n==1:
        print(1)
        return
    print(n)
    print_nums(n-1)
    
print_nums(5)
    
    
