def print_all_subarrays_bruteforce(arr):
    n= len(arr)
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])
            
print(print_all_subarrays_bruteforce([1,2,3]))