def sum_of_all_subarr_Bruteforce(arr):
    n= len(arr)
    total_sum=0
    for i in range(n):
        curr_sum=0
        for j in range(i,n):
            curr_sum= curr_sum+ arr[j]
            total_sum= total_sum+ curr_sum
    return total_sum

print(sum_of_all_subarr_Bruteforce([1,2,3]))