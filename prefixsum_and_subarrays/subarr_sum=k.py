def subarray_sum_equals_k(arr,k):
    n= len(arr)
    prefixsum=0
    seen={0:1}
    count=0
    for j in range(n):
        prefixsum= prefixsum+arr[j]
        needed= prefixsum-k
        if needed in seen:
            count= count+ seen[needed]
        if prefixsum in seen:
            seen[prefixsum]= seen[prefixsum]+1
        else:
            seen[prefixsum]=1
    return count

print(subarray_sum_equals_k([2,3,0,-2,-3,4,-4],0))