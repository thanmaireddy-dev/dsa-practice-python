def max_subarr_sum_Bruteforce(arr):
    n= len(arr)
    maxsum= float('-inf')
    for i in range(n):
        currsum=0
        for j in range(i,n):
            currsum= currsum+ arr[j]
            maxsum= max(maxsum, currsum)
    return maxsum

print(max_subarr_sum_Bruteforce([1,2,3]))