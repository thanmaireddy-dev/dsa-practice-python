def subarray_sum_divisible_by_k(arr, k):
    n= len(arr)
    count=0
    prefixsum=0
    seen= {0:1}
    for i in range(n):
        prefixsum= prefixsum+ arr[i]
        remainder= prefixsum % k
        if remainder<0:
            remainder+=k
        if remainder in seen:
            count= count+ seen[remainder]
            seen[remainder]+=1
        else:
            seen[remainder]=1
    return count

print(subarray_sum_divisible_by_k([4,5,0,-2,-3,1],5))