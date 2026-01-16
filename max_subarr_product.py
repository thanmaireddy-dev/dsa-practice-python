def maximum_subarray_product(arr):
    n= len(arr)
    res= currmax= currmin=0
    for i in range(1,n):
        n= arr[i]
        currmax, currmin= max(n, n*currmax, n*currmin), min(n, n*currmax, n*currmin)
        res= max(res,currmax)
    return res

print(maximum_subarray_product([-2,3,4,-4,-2]))