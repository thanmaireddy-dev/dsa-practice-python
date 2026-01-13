def check_if_arr_is_rotatedNsorted(arr):
    n= len(arr)
    count=0
    for i in range(n):
        if arr[i]> arr[(i+1)%n]:
            count= count+1
            if count>1:
                return False
    return True
                
print(check_if_arr_is_rotatedNsorted([5,1,2,3,4]))   