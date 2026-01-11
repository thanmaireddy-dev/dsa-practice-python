def movezeroes(arr):
    n=len(arr)
    pos=0
    for i in range (n):
        if arr[i]!=0:
            arr[pos]= arr[i]
            pos= pos+1
    while (pos<n):
            arr[pos]=0
            pos= pos+1
    return arr

print(movezeroes([6,0,9,6,0,4,11,0,5]))
            
        
        
        