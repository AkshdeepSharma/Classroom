def flip_horizontal_axis(matrix):
    for i in range(len(matrix) // 2):
        temp = matrix[len(matrix) - (i + 1)]
        temp2 = matrix[i]
        matrix.insert(len(matrix) - i, temp2)
        matrix.insert(i, temp)
        del matrix[len(matrix) - (i + 2)]
        del matrix[i + 1]