def capacity_to_ship_packages_within_d_days(weights, days):
    def can_do(mid, weights, days):
        total_days=1
        currload=0
        for weight in weights:
            currload= currload+ weight
            if currload>mid:
                total_days+=1
                currload=weight
        if total_days<=days:
            return True
        else:
            return False
    
    low=max(weights)
    high=sum(weights)
    result=high
    while (low<=high):
        mid=(low+high)//2
        if can_do(mid, weights, days):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(capacity_to_ship_packages_within_d_days([3,2,2,4,1,4],3))
        