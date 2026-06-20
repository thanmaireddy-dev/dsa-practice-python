def valid_perfect_square(num):
    low=0
    high=num-1
    if num==1:
        return True
    while (low<=high):
        mid= (low+high)//2
        if mid*mid==num:
            return True
        elif mid*mid<num:
            low= mid+1
        else:
            high= mid-1
    return False
    
print(valid_perfect_square(17))