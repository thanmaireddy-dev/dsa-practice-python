def no_of_subarrs_of_size_k_w_avg_gThanOrE_x(arr,k,x):
    n= len(arr)
    left=0
    count=0
    winsum= sum(arr[:k])
    avg= winsum/k
    if avg>=x:
        count= count+1
    for right in range(k,n):
        winsum= winsum+ arr[right]-  arr[left]
        left= left+1
        avg= winsum/k
        if avg>=x:
            count= count+1
    return count

arrr= list(map(int, input("enter the array: ").split()))
k= int(input("enter the subarray size: "))
x= int(input("enter the value of X: "))
print(no_of_subarrs_of_size_k_w_avg_gThanOrE_x(arrr,k,x))


        
    
    