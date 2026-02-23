def insert_intervals(intervals, newInterval):
    intervals.append(newInterval)
    n= len(intervals)
    def get_start(x):
        return x[0]
    intervals.sort(key=get_start)
    merged=[]
    merged.append(intervals[0])
    for i in range(1,n):
        curr_start= intervals[i][0]
        curr_end= intervals[i][1]
        
        if merged[-1][1]>=curr_start:
            merged[-1][1]= max(merged[-1][1], curr_end)
        else:
            merged.append([curr_start, curr_end])
    
    return merged

print(insert_intervals([[1,3],[6,9]],[2,5]))