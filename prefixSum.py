def prefix_sum (arr,a,b):
    n= len(arr)
    prefix= [0]* n
    prefix[0]= arr[0]
    for i in range (1,n):
        prefix[i]= prefix[i-1] + arr[i]
    print("the prefix array is: ", prefix)
    if a==0:
        return prefix[b]
    else:
        return prefix[b]- prefix[a-1]
    
arrr= list(map(int, input("enter the array: ").split()))
A= int(input("enter the value of a: "))
B= int(input("enter the value of b: "))
print(prefix_sum(arrr, A, B))
    