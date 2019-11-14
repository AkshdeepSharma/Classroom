def calculate_area_under_glucose_curve(glucose_readings):
    glucose_area = 0
    for i in range(1, len(glucose_readings)):
        sum_glucose = glucose_readings[i][1] + glucose_readings[i - 1][1]
        total_milliseconds = glucose_readings[i][0] - \
            glucose_readings[i - 1][0]
        glucose_area += (sum_glucose / 2) * total_milliseconds
    return glucose_area / 1000


def main():
    cases = int(input())
    glucose_readings = [list(map(float, input().split()))
                        for _ in range(cases)]
    print(calculate_area_under_glucose_curve(glucose_readings))


if __name__ == "__main__":
    main()
