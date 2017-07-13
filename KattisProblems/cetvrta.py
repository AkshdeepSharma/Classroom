vertex = []
aCounter, bCounter = 0, 0
answer = []

for i in range(3):
    vertex.append(input().split(' '))

if vertex[0][0] == vertex[1][0]:
    answer.append(vertex[2][0])
elif vertex[0][0] == vertex[2][0]:
    answer.append(vertex[1][0])
elif vertex[1][0] == vertex[2][0]:
    answer.append(vertex[0][0])

if vertex[0][1] == vertex[1][1]:
    answer.append(vertex[2][1])
elif vertex[0][1] == vertex[2][1]:
    answer.append(vertex[1][1])
elif vertex[1][1] == vertex[2][1]:
    answer.append(vertex[0][1])

print(' '.join(answer))
