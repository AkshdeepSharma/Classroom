seat_position = input()


def up(seat_position):
    start = seat_position[0]
    seat_position = seat_position[1:]
    res = 0
    for i, val in enumerate(seat_position):
        if (i == 0 and val == start and start == "D") or (i == 0 and val != start and start == "D"):
            res += 1
        elif val == "D":
            res += 2
    return res


def down(seat_position):
    start = seat_position[0]
    seat_position = seat_position[1:]
    res = 0
    for i, val in enumerate(seat_position):
        if (i == 0 and val == start and start == "U") or (i == 0 and val != start and start == "U"):
            res += 1
        elif val == "U":
            res += 2
    return res


def leave(seat_position):
    res = 0
    for i in range(1, len(seat_position)):
        if seat_position[i] != seat_position[i - 1]:
            res += 1
    return res


print(up(seat_position))
print(down(seat_position))
print(leave(seat_position))
