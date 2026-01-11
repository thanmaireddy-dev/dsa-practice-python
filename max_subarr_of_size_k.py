def maximum_subarray_of_size_k(arr,k):
    n= len(arr)
    winsum= sum(arr[:k])
    left=0
    maxsum= float('-inf')
    for right in range(k,n):
        winsum= winsum+ arr[right]- arr[left]
        left= left+1
        maxsum= max(maxsum, winsum)
    return maxsum

arrr= list(map(int, input("enter the array: ").split()))
k= int(input("enter the subarray size: "))
print(maximum_subarray_of_size_k(arrr,k))
