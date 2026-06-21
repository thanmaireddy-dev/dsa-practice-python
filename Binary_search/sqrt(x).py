def sqrt(x):
    if x<2:
        return x
    low=0
    high=x-1
    result=-1
    while (low<=high):
        mid=(low+high)//2
        if mid*mid==x:
            return mid
        elif mid*mid<x:
            low=mid+1
            result=mid
        else:
            high=mid-1
    return result

print(sqrt(8))