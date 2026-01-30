def make_sum_divisible_by_P(arr,p):
    n= len(arr)
    prefixsum=0
    seen= {0:-1}
    minlen= float('inf')
    totalsum= sum(arr)
    remainder= totalsum%p
    if remainder==0:
        return 0
    else:
        for i in range(n):
            prefixsum= (prefixsum+ arr[i])%p
            needed= (prefixsum- remainder+p) %p
            if needed in seen:
                length= i- seen[needed]
                minlen= min(minlen, length)
            seen[prefixsum]=i
    return minlen if minlen<n else -1

print(make_sum_divisible_by_P([1,2,3],3))

    