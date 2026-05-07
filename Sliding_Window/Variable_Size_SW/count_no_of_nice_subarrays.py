def count_no_of_subarr_w_k_odd_numbers(arr,k):
    n= len(arr)
    seen= {0:1}
    prefixsum=0
    count=0
    for i in range(n):
        if arr[i]%2==0:
            arr[i]=0
        else:
            arr[i]=1
        
        prefixsum= prefixsum+ arr[i]
        needed= prefixsum-k
        if needed in seen:
            count= count+ seen[needed]
        if prefixsum in seen:
            seen[prefixsum]+= 1
        else:
            seen[prefixsum]=1
    return count 

print(count_no_of_subarr_w_k_odd_numbers([2,2,2,1,2,2,1,2,2,2],2))