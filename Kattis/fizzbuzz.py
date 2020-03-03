XYN = input().split(' ')
x = int(XYN[0])
y = int(XYN[1])
N = int(XYN[2])

for i in range(1, N + 1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % x == 0:
        print("Fizz")
    elif i % y == 0:
        print("Buzz")
    else:
        print(i)
