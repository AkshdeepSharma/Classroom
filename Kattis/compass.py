def minimumDistance(curr_direction, correct_direction):
    if curr_direction > correct_direction:
        distances = [360 - curr_direction + correct_direction,
                     curr_direction - correct_direction]
    else:
        distances = [correct_direction - curr_direction,
                     360 - correct_direction + curr_direction]
    if abs(distances[0]) <= abs(distances[1]):
        return distances[0]
    return distances[1] * -1


def main():
    curr_direction = int(input())
    correct_direction = int(input())
    print(minimumDistance(curr_direction, correct_direction))


if __name__ == "__main__":
    main()
