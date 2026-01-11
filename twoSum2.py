def two_sum_for_sorted_array(arr, target):
    n= len(arr)
    p1=0
    p2= n-1
    while p1<p2:
        sum= arr[p1]+arr[p2]
        if sum == target:
            return [p1,p2]
        elif sum < target:
            p1 = p1+1
        else:
            p2= p2-1
    return []

arrr= list(map(int, input("enter the sorted array: ").split()))
t= int(input("enter the target number: "))
print(two_sum_for_sorted_array(arrr,t)) 

            