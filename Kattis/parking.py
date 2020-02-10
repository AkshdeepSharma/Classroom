def parking(prices, truck1, truck2, truck3, mini, maxi):
    trucks_parked = -1
    cost = 0
    for i in range(mini, maxi + 1):
        if i in truck1:
            trucks_parked += 1
        if i in truck2:
            trucks_parked += 1
        if i in truck3:
            trucks_parked += 1
        cost += prices[trucks_parked] * (trucks_parked + 1)
        trucks_parked = -1
    return cost


def main():
    prices = list(map(int, input().split()))
    truck1 = list(map(int, input().split()))
    truck2 = list(map(int, input().split()))
    truck3 = list(map(int, input().split()))
    mini = min(truck1[0], truck2[0], truck3[0])
    maxi = max(truck1[1], truck2[1], truck3[1])
    truck1 = set(range(truck1[0], truck1[1]))
    truck2 = set(range(truck2[0], truck2[1]))
    truck3 = set(range(truck3[0], truck3[1]))
    print(parking(prices, truck1, truck2, truck3, mini, maxi))


if __name__ == "__main__":
    main()
