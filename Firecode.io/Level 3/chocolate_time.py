def distribute_chocolate(points):
    count = len(points)
    for i in range(1, len(points)):
        if points[i - 1] != points[i]:
            count += 1
    return count

points = [2, 3, 3, 2, 1, 5, 2]
print(distribute_chocolate(points))

'''
num =    [1, 2, 3, 2, 1, 2, 1]
result = 6
5 to -1


'''