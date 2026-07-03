def painters_partition(arr,k):
    def can_paint(mid, arr,k):
        total_time=0
        painters=1
        for time in arr:
            total_time= total_time+ time
            if total_time>mid:
                painters+=1
                total_time=time
        if painters<=k:
            return True
        else:
            return False
        
    low=max(arr)
    high=sum(arr)
    while (low<=high):
        mid=(low+high)//2
        if can_paint(mid, arr,k):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(painters_partition([5,10, 30, 20, 15],3))