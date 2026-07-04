def minimum_no_of_days_to_make_m_boquets(arr,m,k):
    n=len(arr)
    if n< m*k:
        return -1
    def can_make(mid,arr,m,k):
        flowers=0
        boquets=0
        for flower in arr:
            if flower<=mid:
                flowers+=1
            else:
                flowers=0
            if flowers==k:
                boquets+=1
                flowers=0
        if boquets==m:
            return True
        else:
            return False
        
    low=min(arr)
    high=max(arr)
    while (low<=high):
        mid=(low+high)//2
        if can_make(mid,arr,m,k):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(minimum_no_of_days_to_make_m_boquets([7,7,7,7,12,7,7],2,3))
    