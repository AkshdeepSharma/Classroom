def flip_horizontal_axis(matrix):
    count = len(matrix)
    for i in range(len(matrix) - 1, -1, -1):
        matrix.append(matrix[i])
    for j in range(count):
        del matrix[0]