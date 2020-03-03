pos = input().split(" ")
pos0 = int(pos[0])
pos1 = int(pos[1])
pos2 = int(pos[2])

if pos1 - pos0 < pos2 - pos1:
    if pos2 - pos1 - 1 >= 0:
        print(pos2 - pos1 - 1)
    else:
        print(0)
else:
    if pos1 - pos0 - 1 >= 0:
        print(pos1 - pos0 - 1)
    else:
        print(0)
