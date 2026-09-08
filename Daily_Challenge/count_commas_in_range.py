def count_commas(n):
    if n<1000:
        return 0
    else:
        return n-999
    
print(count_commas(1002))