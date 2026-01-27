def count_subarrays_with_sum_zero(arr):
    n= len(arr)
    seen={0:1}
    prefixsum=0
    count=0
    for i in range(n):
        prefixsum= prefixsum+arr[i]
        if prefixsum in seen:
            count= count+ seen[prefixsum]
            seen[prefixsum]+=1
        else:
            seen[prefixsum]=1
    return count

print(count_subarrays_with_sum_zero([2,3,0,-2,-3,4,-4]))
        
        