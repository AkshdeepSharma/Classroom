def main():
    scores = {}
    winners = []
    winners_set = set()
    participants, points_to_win, scored_points = map(int, input().split())
    for _ in range(participants):
        scores[input()] = 0
    for _ in range(scored_points):
        name, points = input().split()
        scores[name] += int(points)
        if scores[name] >= points_to_win and name not in winners_set:
            winners.append(name)
            winners_set.add(name)
    if not winners:
        print("No winner!")
    else:
        for name in winners:
            print(f"{name} wins!")


if __name__ == "__main__":
    main()
