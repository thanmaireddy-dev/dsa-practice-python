def koko_eating_bananananananana(piles,h):
    def can_eat(mid, piles,h):
        total_hours=0
        for pile in piles:
            total_hours=total_hours+(pile+mid-1)//mid
        if total_hours<=h:
            return True
        return False
    
    low=1
    high=max(piles)
    result=high
    while (low<=high):
        mid=(low+high)//2
        if can_eat(mid,piles,h):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(koko_eating_bananananananana([30,11,23,4,20],6))