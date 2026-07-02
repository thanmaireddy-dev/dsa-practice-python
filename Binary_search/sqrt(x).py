def sqrt(x):
    if x<2:
        return x
    low=1
    high=x
    while (low<=high):
        mid=(low+high)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            result=mid
            low=mid+1
        else:
            high=mid-1
    return result

print(sqrt(8))