def main():
    num_trips = int(input())
    trips = {}
    for _ in range(num_trips):
        place, year = input().split()
        if place not in trips:
            trips[place] = [int(year)]
        else:
            trips[place].append(int(year))
    for val in trips.values():
        val.sort()
    num_queries = int(input())
    for _ in range(num_queries):
        place, query = input().split()
        print(trips[place][int(query) - 1])


if __name__ == "__main__":
    main()
