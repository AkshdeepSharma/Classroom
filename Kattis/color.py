def minWashingMachinesNeeded(socks, capacity, diff):
    washing_machines = 0
    socks = sorted(socks)
    start = i = num_socks = 0
    while i < len(socks):
        num_socks += 1
        if socks[i] - socks[start] > diff:
            start = i
            num_socks = 1
            washing_machines += 1
        elif num_socks == capacity:
            start = i + 1
            num_socks = 0
            washing_machines += 1
        if i == len(socks) - 1 and num_socks > 0:
            washing_machines += 1
        i += 1
    return washing_machines


def main():
    S, C, K = map(int, input().split())
    socks = map(int, input().split())
    print(minWashingMachinesNeeded(socks, C, K))


if __name__ == "__main__":
    main()
