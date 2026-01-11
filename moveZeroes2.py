def move_zeroes(arr):
    n= len(arr)
    p1=0
    for i in range(n):
        if arr[i]!=0:
            arr[p1]= arr[i]
            p1= p1+1
    for j in range (p1, n):
        arr[j]=0
    return arr

print(move_zeroes([2,0,40,4,0,4,0,5,0]))