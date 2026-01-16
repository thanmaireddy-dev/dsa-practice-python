def max_subarr_product_Bruteforce(arr):
    n= len(arr)
    maxprod= float('-inf')
    for i in range(n):
        currprod=1
        for j in range(i,n):
            currprod= currprod * arr[j]
            maxprod= max(maxprod, currprod)
    return maxprod

print(max_subarr_product_Bruteforce([-2,0,-1]))