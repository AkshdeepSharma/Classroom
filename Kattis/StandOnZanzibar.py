testCases = int(input())

for i in range(testCases):
    numberOfTurtles = 0
    turtles = input().split(' ')
    for j in range(len(turtles)):
        if int(turtles[j]) > int(turtles[j + 1]):
            break
        elif int(turtles[j]) * 2 < int(turtles[j + 1]):
            numberOfTurtles += ((int(turtles[j+ 1])) - (int(turtles[j]) * 2))
    print(numberOfTurtles)
