def main():
    num_planets = int(input())
    for _ in range(num_planets):
        P, R, F = map(int, input().split())
        print(planetSustainabilityLength(P, R, F))


def planetSustainabilityLength(P, R, F):
    years = 0
    while P <= F:
        years += 1
        P *= R
    return years


if __name__ == "__main__":
    main()
