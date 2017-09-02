matrix = [[1,2],[3,4]]


def find_spiral(matrix):
    output_list = []
    while len(matrix) != 1:
        output_list.append(matrix[0])
        matrix = matrix[1:]
        m = len(matrix)
        n = len(matrix[0])

        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[j][i])
            matrix.append(temp)

        for _ in range(m):
            del matrix[0]

        for k in range(len(matrix) - 1, -1, -1):
            matrix.append(matrix[k])

        for _ in range(n):
            del matrix[0]

    output_list.append(matrix[0])
    output_list = [q for p in output_list for q in p]
    return output_list

print(find_spiral(matrix))