def non_overlapping_intervals(intervals):
    n= len(intervals)
    count=0
    def get_end(x):
        return x[1]
    intervals.sort(key=get_end)
    prev_end= intervals[0][1]
    for i in range(1,n):
        curr_start= intervals[i][0]
        curr_end= intervals[i][1]
        if prev_end>=curr_start:
            count= count+1
        else:
            prev_end= curr_end
    return count

print(non_overlapping_intervals([[1,3],[2,4],[3,5]]))
            

    
    
    
    
    