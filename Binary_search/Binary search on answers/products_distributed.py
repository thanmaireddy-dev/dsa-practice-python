import math
def minimized_maximum_of_products_distributed_to_any_store(n, quantities):
    def can_distribute(mid, n, quantities):
        slots=0
        for num in quantities:
            slots= slots+ math.ceil(float(num)/mid) #orrrr use slots+ (num+mid-1)//mid
        if slots<=n:
            return True
        else:
            return False
    
    low=1
    high= max(quantities)
    while (low<=high):
        mid=(low+high)//2
        if can_distribute(mid,n, quantities):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(minimized_maximum_of_products_distributed_to_any_store(6, [11,6]))
    