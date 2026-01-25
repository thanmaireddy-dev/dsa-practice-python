def prefix_sum(arr,a,b):
    n= len(arr)
    prefix= [0]*n
    prefix[0]= arr[0]
    for i in range(n):
        prefix[i]= prefix[i-1]+arr[i]
    if a==0:
        return prefix[b]
    else:
        return prefix[b]- prefix[a-1]
    
print(prefix_sum([4,2,-3,-1,2,6], 0, 2))
 

    
    
    