def rotate_array_optimal(arr,k):
    n=len(arr)
    arr2= [0]*n
    for i in range(n):
        arr2[(i+k)%n]= arr[i]
    return arr2

print(rotate_array_optimal([1,2,3,4,5,6,7],3))