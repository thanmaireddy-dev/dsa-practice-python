def reverse_an_array(arr):
    n= len(arr)
    p1=0
    p2=n-1
    while (p1<=p2):
        arr[p1], arr[p2]= arr[p2], arr[p1]
        p1= p1+1
        p2= p2-1
    return arr 

arrr= list(map(int, input().split()))
print(reverse_an_array(arrr))
    
    
        
        