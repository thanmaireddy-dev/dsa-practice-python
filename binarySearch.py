def binary_search(arr, target):
    low=0
    high= len(arr)-1
    while (high>=low):
        mid = (high+low)//2
        if arr[mid]== target:
            return mid
        elif arr[mid]< target:
            low= mid+1
        else:
            high= mid-1
    return -1
            

arrr= list(map(int, input().split()))
targett= int(input())
print(binary_search(arrr, targett))
            
            
        