def subarray_sum_equals_k(arr,k):
    n= len(arr)
    count=0
    for i in range(n):
        currsum=0
        for j in range(i,n):
            currsum= currsum+ arr[j]
            if currsum==k:
                count= count+1
    return count 

arrr= list(map(int, input("enter the array: ").split()))
p= int(input("enter the target: "))
print(subarray_sum_equals_k(arrr, p))