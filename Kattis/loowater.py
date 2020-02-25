def getMinGoldRequired(head_diameters, knight_heights):
    gold = 0
    j = 0
    if len(head_diameters) > len(knight_heights):
        return "Loowater is doomed!"
    for head in head_diameters:
        try:
            while True:
                if knight_heights[j] >= head:
                    gold += knight_heights[j]
                    j += 1
                    break
                j += 1
        except IndexError:
            return "Loowater is doomed!"
    return gold


def main():
    heads, knights = map(int, input().split())
    while heads + knights != 0:
        head_diameters = sorted([int(input()) for _ in range(heads)])
        knight_heights = sorted([int(input()) for _ in range(knights)])
        print(getMinGoldRequired(head_diameters, knight_heights))
        heads, knights = map(int, input().split())


if __name__ == "__main__":
    main()
