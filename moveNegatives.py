def move_negatives(arr):
    left = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[left], arr[i] = arr[i], arr[left]
            left= left+1
    return arr


print(move_negatives([-1,3,-3,4,-5,2,0,-4]))
        

