def kadanes_bruteforce(arr):
    n= len(arr)
    maxsum= float('-inf')
    currsum=0
    for i in range(n):
        currsum=0
        for j in range(i,n):
            currsum= currsum+ arr[j]
            maxsum= max(currsum, maxsum)
    return maxsum

arrr= list(map(int, input("enter the array ").split()))
print(kadanes_bruteforce(arrr))