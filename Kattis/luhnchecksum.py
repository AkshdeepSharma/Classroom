def check_sum(card):
    card_sum = 0
    for i in range(len(card) - 2, -1, -2):
        card[i] = card[i] * 2
    for num in card:
        card_sum += num // 10
        card_sum += num % 10
    return "PASS" if card_sum % 10 == 0 else "FAIL"


def main():
    N = int(input())
    for _ in range(N):
        card_number = list(map(int, list(input())))
        print(check_sum(card_number))


if __name__ == "__main__":
    main()
