def linear_search(arr, target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1

print(linear_search([2,5,3,6,5], 6))


    