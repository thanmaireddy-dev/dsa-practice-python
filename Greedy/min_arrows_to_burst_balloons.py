def minimum_number_of_arrows_to_burst_balloons(points):
    n= len(points)
    def get_end(x):
        return x[1]
    points.sort(key=get_end)
    arrow_pos= points[0][1]
    arrows=1
    for i in range( 1,n):
        curr_start= points[i][0]
        curr_end= points[i][1]
        if arrow_pos>=curr_start:
            pass
        else:
            arrow_pos= curr_end
            arrows= arrows+1
    return arrows

        
        
     