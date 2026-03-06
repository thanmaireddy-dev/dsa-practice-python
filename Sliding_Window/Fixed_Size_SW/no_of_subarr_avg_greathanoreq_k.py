def number_of_subarrays_of_size_k_and_average_GorEto_threshold(arr, k, threshold):
    n= len(arr)
    left=0
    count=0
    winsum= sum(arr[:k])
    avg= winsum/k
    if avg>= threshold:
        count= count+1
    
    for right in range(k,n):
        winsum= winsum+ arr[right]- arr[left]
        left= left+1
        avg= winsum/k
        if winsum>= threshold:
            count= count+1
    return count
        
print(number_of_subarrays_of_size_k_and_average_GorEto_threshold([2,2,2,2,5,5,5,8],3,4))   
        
    