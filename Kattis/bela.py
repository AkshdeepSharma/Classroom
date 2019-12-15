def main():
    N, dominant_suit = input().split()
    points = 0
    for _ in range(int(N) * 4):
        card = input()
        if card[1] == dominant_suit:
            points += dominant[card[0]]
        else:
            points += non_dominant[card[0]]
    print(points)


if __name__ == '__main__':
    dominant = {
        "A": 11,
        "K": 4,
        "Q": 3,
        "J": 20,
        "T": 10,
        "9": 14,
        "8": 0,
        "7": 0
    }
    non_dominant = {
        "A": 11,
        "K": 4,
        "Q": 3,
        "J": 2,
        "T": 10,
        "9": 0,
        "8": 0,
        "7": 0
    }
    main()
