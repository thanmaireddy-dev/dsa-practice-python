def rotate_array(arr,k):
    n= len(arr)
    p1=0
    p2= n-1
    for i in range(k):
        arr.insert(0,arr[p2])
        arr.pop()
    return arr

print(rotate_array([-1,-100,3,99],2))
    