def find_min_max_in_array(arr):
    n=len(arr)
    min=0
    max=0
    for i in range(n):
        if arr[i]<min:
            min=i
        if arr[i]> max:
            max= i
    return arr[min], arr[max]

print(find_min_max_in_array([8,9,0,45]))