def smallest_subarr_w_sum_gThanOrE_target(arr, target):
    n= len(arr)
    left=0
    currsum=0
    minlen= float('inf')
    for right in range(n):
        currsum= currsum+ arr[right]
        while currsum>= target:
            currsum= currsum- arr[left]
            minlen= min(minlen, right-left+1)
            left= left+1
    return minlen if minlen!= float('inf') else 0

arrr= list(map(int, input("enter the array: ").split()))
t= int(input("enter the target: "))
print(smallest_subarr_w_sum_gThanOrE_target(arrr, t))


            
        
        
        
    