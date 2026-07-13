def search_a_2d_matrix(matrix, target):
    def search_row(matrix, target, midrow):
        n= len(matrix[0])
        low=0
        high=n-1
        while (low<=high):
            mid=(low+high)//2
            if matrix[midrow][mid]==target:
                return True
            elif matrix[midrow][mid]<target:
                low=mid+1
            else:
                high=mid-1
        return False

    rows=len(matrix)
    columns= len(matrix[0])
    startrow=0
    endrow=rows-1
    while (startrow<=endrow):
        midrow= (startrow+ endrow)//2
        if matrix[midrow][0]<=target<= matrix[midrow][columns-1]:
            return search_row(matrix, target, midrow)
        elif target> matrix[midrow][columns-1]:
            startrow= midrow+1
        else:
            endrow= midrow-1
    return False

print(search_a_2d_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],344))