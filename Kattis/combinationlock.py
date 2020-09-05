def findDegreesRotated(combo):
    degrees_rotated = (abs(combo[0] - combo[1] + 40) % 40) * 9
    degrees_rotated += (abs(combo[2] - combo[1] + 40) % 40) * 9
    degrees_rotated += (abs(combo[2] - combo[3] + 40) % 40) * 9
    return 1080 + degrees_rotated


def main():
    combo = list(map(int, input().split()))
    while combo != [0, 0, 0, 0]:
        print(findDegreesRotated(combo))
        combo = list(map(int, input().split()))


if __name__ == '__main__':
    main()
