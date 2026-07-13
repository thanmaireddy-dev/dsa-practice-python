def search_a_2d_matrix_II(matrix, target):
    rows=len(matrix)
    columns= len(matrix[0])
    r=0
    c=columns-1
    while (r<rows and c>=0):
        if matrix[r][c]==target:
            return True
        elif matrix[r][c]<target:
            r=r+1
        else:
            c=c-1
    return False

print(search_a_2d_matrix_II([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],23))