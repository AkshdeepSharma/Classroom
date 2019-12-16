def main():
    cards = input().split()
    count = 0
    cards = [card[0] for card in cards]
    for card in cards:
        count = max(cards.count(card), count)
    print(count)


if __name__ == '__main__':
    main()
