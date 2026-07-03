def aggresive_cows(arr,k):
    arr.sort()
    n=len(arr)
    def can_place(mid,arr,k):
        cows=1
        last_pos=arr[0]
        for i in range(n):
            if (arr[i]-last_pos)>=mid:
                cows=cows+1
                last_pos=arr[i]
        if cows>=k:
            return True
        else:
            return False
    
    low=1
    high=max(arr)-min(arr)
    while (low<=high):
        mid=(low+high)//2
        if can_place(mid, arr,k):
            result=mid
            low=mid+1
        else:
            high=mid-1
    return result

print(aggresive_cows([1 ,2 ,4 ,8 ,9],3))
        