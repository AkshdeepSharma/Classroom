matrix = [[1,2,3], [4,5,6], [7,8,9]]


def transpose_matrix(matrix):
    count = len(matrix)
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[i])):
            temp.append(matrix[j][i])
        matrix.append(temp)
    for k in range(count):
        del matrix[0]

transpose_matrix(matrix)
print(matrix)