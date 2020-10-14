def correctTime(direction, change, hours, mins):
    if direction == 'F':
        mins += change
    elif direction == 'B':
        mins -= change
    for _ in range(2):
        if mins < 0:
            mins += 60
            hours -= 1
        elif mins >= 60:
            mins -= 60
            hours += 1
    if hours > 23:
        hours -= 24
    elif hours < 0:
        hours += 24
    return f'{hours} {mins}'


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        inp = input().split()
        direction, change, hours, mins = inp[0], int(
            inp[1]), int(inp[2]), int(inp[3])
        print(correctTime(direction, change, hours, mins))


if __name__ == "__main__":
    main()
