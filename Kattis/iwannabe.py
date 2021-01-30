def getTeamSize(attack, defense, health, K):
    team = set()
    for i in range(K):
        if attack[i][1] not in team:
            team.add(attack[i][1])
        if defense[i][1] not in team:
            team.add(defense[i][1])
        if health[i][1] not in team:
            team.add(health[i][1])
    return len(team)


def main():
    N, K = list(map(int, input().split()))
    attack, defense, health = [], [], []
    for i in range(N):
        a, d, h = list(map(int, input().split()))
        attack.append([a, i])
        defense.append([d, i])
        health.append([h, i])
    attack = sorted(attack, reverse=True)
    defense = sorted(defense, reverse=True)
    health = sorted(health, reverse=True)
    print(getTeamSize(attack, defense, health, K))


if __name__ == '__main__':
    main()
