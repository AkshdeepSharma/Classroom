def makeItToClassOnTime(leave_house_time, class_start_time, buses_to_take, walking_times, time_on_buses, bus_arival_times):
    curr_time = leave_house_time
    for i in range(buses_to_take):
        curr_time += walking_times[i]
        add_time = bus_arival_times[i]
        while bus_arival_times[i] < curr_time:
            bus_arival_times[i] += add_time
        curr_time = bus_arival_times[i] + time_on_buses[i]
    curr_time += walking_times[-1]
    return 'yes' if curr_time <= class_start_time else 'no'


def main():
    leave_house_time, class_start_time, buses_to_take = map(
        int, input().split())
    walking_times = list(map(int, input().split()))
    time_on_buses = list(map(int, input().split()))
    bus_arival_times = list(map(int, input().split()))
    print(makeItToClassOnTime(leave_house_time, class_start_time,
                              buses_to_take, walking_times, time_on_buses, bus_arival_times))


if __name__ == "__main__":
    main()
