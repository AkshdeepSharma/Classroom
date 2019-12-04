def main():
    sequence = input()
    cups = [1, 2, 3]
    for move in sequence:
        if move == "A":
            cups[0], cups[1] = cups[1], cups[0]
        elif move == "B":
            cups[1], cups[2] = cups[2], cups[1]
        else:
            cups[0], cups[2] = cups[2], cups[0]
    print(cups.index(1) + 1)


if __name__ == '__main__':
    main()
