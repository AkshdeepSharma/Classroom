tri = input().split(' ')
a = int(tri[0])
b = int(tri[1])
c = int(tri[2])

if (a + b) == c:
    print(str(a) + '+' + str(b) + '=' + str(c))
elif a == (b + c):
    print(str(a) + '=' + str(b) + '+' + str(c))
elif (a - b) == c:
    print(str(a) + '-' + str(b) + '=' + str(c))
elif a == (b - c):
    print(str(a) + '=' + str(b) + '-' + str(c))
elif (a * b) == c:
    print(str(a) + '*' + str(b) + '=' + str(c))
elif a == (b * c):
    print(str(a) + '=' + str(b) + '*' + str(c))
elif (a / b) == c:
    print(str(a) + '/' + str(b) + '=' + str(c))
elif a == (b / c):
    print(str(a) + '=' + str(b) + '/' + str(c))
