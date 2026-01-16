def kadanes_algo(arr):
    n= len(arr)
    maxsum= float('-inf')
    currsum=0
    for i in range(n):
        if currsum<0:
            currsum=0
        currsum= currsum+ arr[i]
        maxsum= max(maxsum, currsum)
    return maxsum

print(kadanes_algo([1,2,3,-10,2,3,6]))