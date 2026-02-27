def meeting_rooms_2(intervals):
    starts=[]
    ends=[]
    for interval in intervals:
        starts.append(interval[0])
        ends.append(interval[1])
    starts.sort()
    ends.sort()
    
    i=j=0
    rooms_in_use=0
    max_rooms=0
    n= len(starts)
    while i<n:
        if starts[i]<ends[j]:
            rooms_in_use+=1
            max_rooms= max(max_rooms, rooms_in_use)
            i=i+1
        else:
            rooms_in_use-=1
            j=j+1
    return max_rooms
    
    
print(meeting_rooms_2([[0,40], [5,10], [15,20]]))
    
