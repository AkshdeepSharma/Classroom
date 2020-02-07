def wastedVotes(votes, D):
    res = []
    wasted_A = wasted_B = 0
    for i in range(1, D + 1):
        votesA, votesB = votes[i][0], votes[i][1]
        needed = (votesA + votesB) // 2 + 1
        if votesA > votesB:
            temp = "A " + str(votesA - needed) + " " + str(votesB)
            wasted_A += votesA - needed
            wasted_B += votesB
        else:
            temp = "B " + str(votesA) + " " + str(votesB - needed)
            wasted_A += votesA
            wasted_B += votesB - needed
        res.append(temp)
    return res, wasted_A, wasted_B


def efficiencyGap(wasted_A, wasted_B, total_votes):
    return round(abs(wasted_A - wasted_B) / total_votes, 10)


def main():
    P, D = map(int, input().split())
    votes = {}
    total_votes = 0
    for i in range(1, D + 1):
        votes[i] = [0, 0]
    for i in range(P):
        district = list(map(int, input().split()))
        votes[district[0]][0] += district[1]
        votes[district[0]][1] += district[2]
        total_votes += district[1] + district[2]

    precinct_results, wasted_A, wasted_B = wastedVotes(votes, D)
    for res in precinct_results:
        print(res)
    print(efficiencyGap(wasted_A, wasted_B, total_votes))


if __name__ == "__main__":
    main()
