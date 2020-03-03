from collections import defaultdict
while True:
    inputs = input().split()
    if len(inputs) == 1:
        break
    players, games = int(inputs[0]), int(inputs[1])
    d = defaultdict(int)
    for i in range((players * games * (players - 1)) // 2):
        line = input().split()
        playerA, playerAMove, playerB, playerBMove = line[0], line[1], line[2], line[3]
        if playerAMove != playerBMove:
            if (playerAMove == "paper" and playerBMove == "rock") or (playerAMove == "scissors" and playerBMove == "paper") or (playerAMove == "rock" and playerBMove == "scissors"):
                d[playerA] += 1
            else:
                d[playerB] += 1
            d[playerA+"g"] += 1
            d[playerB+"g"] += 1

    for i in range(1, players + 1):
        if str(i)+"g" not in d:
            print("-")
        else:
            print("{:.3f}".format(d[str(i)] / d[str(i)+"g"]))
    print("")
