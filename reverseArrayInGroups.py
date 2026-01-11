def reverse_array_in_groups_of_k(arr,k):
    n= len(arr)
    for i in range(0,n,k):
        left= i
        right= min(i+k-1, n-1)
        while (left<right):
            arr[left], arr[right]= arr[right], arr[left]
            left= left+1
            right= right-1
    return arr

print(reverse_array_in_groups_of_k([1,2,3,4,5,6,7,8], 3))