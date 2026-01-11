def find_avg_of_all_subarrays_of_size_k(arr,k):
    n= len(arr)
    left=0
    result= []
    winsum= sum(arr[:k])
    result.append(winsum/k)
    for right in range(k,n):
        winsum= winsum+ arr[right] - arr[left]
        left= left+ 1
        result.append(winsum/k)
    return result

arrr= list(map(int, input("enter the array: ").split()))
k= int(input("enter the subarray size: "))
print(find_avg_of_all_subarrays_of_size_k(arrr,k))
        
    