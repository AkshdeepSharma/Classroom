import math as m

N = int(input())

for i in range(N):
    parameters = input().split(' ')
    v0, theta, distance, h1, h2 = float(parameters[0]), m.radians(float(parameters[1])), float(parameters[2]), \
        float(parameters[3]), float(parameters[4])
    g = 9.81
    time = distance / (v0 * m.cos(theta))
    yheight = v0 * time * m.sin(theta) - 0.5 * g * time ** 2
    if yheight + 1 <= h2 and yheight - 1 >= h1:
        print('Safe')
    else:
        print('Not Safe')
