def optimal_parking(store_locations):
    return (max(store_locations) - min(store_locations)) * 2


def main():
    t = int(input())
    for _ in range(t):
        num_stores = int(input())
        store_locations = list(map(int, input().split(" ")))
        print(optimal_parking(store_locations))


if __name__ == "__main__":
    main()
