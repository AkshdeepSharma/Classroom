def minTotalDistance(distances):
    best = min(distances[-2] + distances[0], distances[-1] + distances[1])
    for i in range(len(distances) - 2):
        best = min(distances[i] + distances[i + 2], best)
    return best


def main():
    runners = int(input())
    distances = [int(input()) for _ in range(runners)]
    print(minTotalDistance(distances))


if __name__ == "__main__":
    main()
