def maximum_candies_allocated_to_k_children(candies,k):
    if sum(candies)<k:
        return 0
    def can_allocate(mid, candies,k):
        piles=0
        for num in candies:
            piles= piles+ (num//mid)
        if piles>=k:
            return True
        else:
            return False 
        
    low=1
    high=max(candies)
    while (low<=high):
        mid=(low+high)//2
        if can_allocate(mid, candies,k):
            result=mid
            low=mid+1
        else:
            high=mid-1
    return result

print(maximum_candies_allocated_to_k_children([5,8,6],3))
        