def findSpeedConstant(time, distances, speeds, num_segments):
    min_constant, max_constant = 0 - min(speeds), 1001000
    while round(min_constant, 6) != round(max_constant, 6):
        curr_time = 0
        mid_constant = (min_constant + max_constant) / 2
        for i in range(num_segments):
            curr_time += distances[i] / (speeds[i] + mid_constant)
        if curr_time > time:
            min_constant = mid_constant
        elif curr_time < time:
            max_constant = mid_constant
    return f"{round(min_constant, 6)}"


def main():
    num_segments, time = map(int, input().split())
    distances = []
    speeds = []
    for _ in range(num_segments):
        segment = list(map(int, input().split()))
        distances.append(segment[0])
        speeds.append(segment[1])
    print(findSpeedConstant(time, distances, speeds, num_segments))


if __name__ == "__main__":
    main()
