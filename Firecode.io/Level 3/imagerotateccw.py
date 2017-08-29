matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def rotate_square_image_ccw(matrix):
    count = len(matrix)
    for i in range(len(matrix)):
        temp = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            temp.append(matrix[i][j])
        matrix.append(temp)
    for x in range(count):
        del matrix[0]
    for k in range(len(matrix)):
        temp2 = []
        for l in range(len(matrix[0])):
            temp2.append(matrix[l][k])
        matrix.append(temp2)
    for y in range(count):
        del matrix[0]

print(rotate_square_image_ccw(matrix))