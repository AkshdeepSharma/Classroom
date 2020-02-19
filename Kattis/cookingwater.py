def isPotBoilingAtSameTime(time_interval_list):
    curr_set = time_interval_list[0]
    for i in range(1, len(time_interval_list)):
        curr_set = curr_set.intersection(time_interval_list[i])
    if curr_set:
        return "gunilla has a point"
    return "edward is right"


def main():
    num_of_time_intervals = int(input())
    time_interval_list = []
    for _ in range(num_of_time_intervals):
        interval = list(map(int, input().split()))
        interval_set = {i for i in range(interval[0], interval[1] + 1)}
        time_interval_list.append(interval_set)
    print(isPotBoilingAtSameTime(time_interval_list))


if __name__ == "__main__":
    main()
