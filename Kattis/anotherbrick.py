def goodBricks(bricks, h, w):
    curr = 0
    for i in range(len(bricks)):
        curr += bricks[i]
        if curr == w:
            curr = 0
            if h - 1 == 0:
                return "YES"
            h -= 1
        if curr > w:
            return "NO"


def main():
    h, w, n = map(int, input().split())
    bricks = list(map(int, input().split()))
    print(goodBricks(bricks, h, w))


if __name__ == "__main__":
    main()
