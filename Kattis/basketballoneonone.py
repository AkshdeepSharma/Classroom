def get_winner(score_string):
    A, B = 0, 0
    for i in range(0, len(score_string), 2):
        player, points = score_string[i], int(score_string[i + 1])
        if player == "A":
            A += points
        else:
            B += points
        if A > 10 and A - B > 1:
            return "A"
        elif B > 10 and B - A > 1:
            return "B"


def main():
    score_string = input()
    print(get_winner(score_string))


if __name__ == '__main__':
    main()
