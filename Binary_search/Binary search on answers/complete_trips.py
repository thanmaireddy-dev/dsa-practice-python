def minimum_time_to_complete_trips(time, totalTrips):
    def can_go(mid, time, totalTrips):
        trips=0
        for num in time:
            trips= trips+ (mid//num)
        if trips>=totalTrips:
            return True
        else:
            return False
        
    low=min(time)
    high=min(time)*totalTrips
    while (low<=high):
        mid=(low+high)//2
        if can_go(mid, time, totalTrips):
            result=mid
            high=mid-1
        else:
            low=mid+1
    return result

print(minimum_time_to_complete_trips([1,2,3],5))
        