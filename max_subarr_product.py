def maximum_subarray_product(arr):
    res= currmax= currmin=arr[0]
    for i in range(1,len(arr)):
        n= arr[i]
        currmax, currmin= max(n, n*currmax, n*currmin), min(n, n*currmax, n*currmin)
        res= max(res,currmax)
    return res

print(maximum_subarray_product([-2,3,4,-4,-2]))