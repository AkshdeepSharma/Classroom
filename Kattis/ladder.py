import math as m

hv = input().split(' ')
opposite = int(hv[0])
angle = m.radians(int(hv[1]))

print(m.ceil(opposite / (m.sin(angle))))
