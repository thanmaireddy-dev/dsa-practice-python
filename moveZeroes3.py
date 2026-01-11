def move_zeroes(arr):
    n= len(arr)
    left=0
    for i in range(n):
        if arr[i]!=0:
            arr[i], arr[left]= arr[left], arr[i]
            left= left+1
    return arr

print(move_zeroes([2,0,3,0,4,0,1,0]))