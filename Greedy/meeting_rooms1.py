def meeting_rooms_1(intervals):
    if not intervals:
        return True
    n= len(intervals)
    def get_start(x):
        return x[0]
    intervals.sort(key=get_start)
    end_time= intervals[0][1]
    for i in range(1,n):
        curr_start= intervals[i][0]
        curr_end= intervals[i][0]
        if end_time>curr_start:
            return False
        else:
            end_time= curr_end
    return True

print(meeting_rooms_1([[2,5],[7,9]]))
    
    
    