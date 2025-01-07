# this does not work for non square matrix
def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
   
    for row in matrix:  
        row.reverse()  
    return matrix

matrix = [[2,3],[5,6],[8,9]]
# print(rotate(matrix))

# rotate non square matrix
def rotate_nonsquare(matrix):
    transpose = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        transpose.append(new_row)
    
    for row in transpose:
        row.reverse()
    return transpose
        
matrix = [[2,3],[5,6],[8,9]]
print(rotate_nonsquare(matrix)) 