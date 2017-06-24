T = int(input())

for i in range(T):
    n = int(input())
    candidate = []
    for j in range(n):
        vote = int(input())
        candidate.append(vote)
    candidateSorted = sorted(candidate, reverse=True)
    if candidateSorted[0] == candidateSorted[1]:
        print('no winner')
    elif candidateSorted[0] > (sum(candidateSorted) - candidateSorted[0]):
        print('majority winner', candidate.index(candidateSorted[0]) + 1)
    else:
        print('minority winner', candidate.index(candidateSorted[0]) + 1)
