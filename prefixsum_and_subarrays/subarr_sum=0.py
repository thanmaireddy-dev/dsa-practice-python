def subarray_sum_equals_zero(arr):
    n= len(arr)
    prefixsum=0
    seen={}
    for i in range(n):
        prefixsum= prefixsum+arr[i]
        if prefixsum==0 or prefixsum in seen:
            return True
        seen[prefixsum]=i
    return False 

print(subarray_sum_equals_zero([2,3,4,-7,2]))