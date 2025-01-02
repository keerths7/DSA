def transpose(matrix):
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            matrix[j][i] = matrix[i][j]
    return matrix

matrix = [[2,3,4],[5,6,7]]
print(transpose(matrix))