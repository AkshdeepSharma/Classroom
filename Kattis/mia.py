def getWinner(roll):
    winner = None
    p1_rolls = set([roll[0] + roll[1], roll[1] + roll[0]])
    p2_rolls = set([roll[2] + roll[3], roll[3] + roll[2]])
    if ('21' in p1_rolls or '12' in p1_rolls) and ('21' not in p2_rolls or '12' not in p2_rolls):
        return "Player 1 wins."
    if ('21' in p2_rolls or '21' in p2_rolls) and ('21' not in p1_rolls or '12' not in p1_rolls):
        return "Player 2 wins."
    if ('21' in p1_rolls or '12' in p1_rolls) and ('21' in p2_rolls or '21' in p2_rolls):
        return "Tie."
    if len(p1_rolls) == 1 and len(p2_rolls) == 2:
        return "Player 1 wins."
    if len(p1_rolls) == 2 and len(p2_rolls) == 1:
        return "Player 2 wins."
    if len(p1_rolls) == 1 and len(p2_rolls) == 1:
        num1, num2 = int(roll[0] + roll[1]), int(roll[2] + roll[3])
        if num1 > num2:
            return "Player 1 wins."
        if num1 < num2:
            return "Player 2 wins."
        return "Tie."
    if int(max(p1_rolls)) > int(max(p2_rolls)):
        return "Player 1 wins."
    elif int(max(p1_rolls)) < int(max(p2_rolls)):
        return "Player 2 wins."
    return "Tie."


def main():
    roll = input().split()
    while roll[0] != '0':
        print(getWinner(roll))
        roll = input().split()


if __name__ == "__main__":
    main()
