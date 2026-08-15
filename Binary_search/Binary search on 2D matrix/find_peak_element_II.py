def find_peak_element_II(matrix):
    rows= len(matrix)
    columns= len(matrix[0])
    low=0
    high=columns-1
    #choose a mid column first
    while (low<=high):
        midcol= (low+high)//2
        #now choose an element which is greater than all of the elements in the same column.
        maxrow=0
        for i in range(1,rows):
            if matrix[i][midcol]> matrix[maxrow][midcol]:
                maxrow=i
                
        left_neighbour= matrix[maxrow][midcol-1] if (midcol>0) else -1
        right_neighbour= matrix[maxrow][midcol+1] if (midcol<columns-1) else -1
        
        if matrix[maxrow][midcol]> left_neighbour and matrix[maxrow][midcol]> right_neighbour:
            return [maxrow, midcol]
        elif matrix[maxrow][midcol]< left_neighbour:
            high= midcol-1
        else:
            low=midcol+1
    return [-1,-1]

print(find_peak_element_II([[8,36,35,17,48],[38,28,38,26,24],[15,9,33,32,6],[49,4,8,10,41]]))

        