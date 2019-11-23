def find_x_coord(a, b):
    return -b / (2 * a)


def find_y_coord(a, b, c, x):
    return (a * x ** 2) + (b * x) + c


def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        num_gears = int(input())
        max_torque_gear = 0
        max_torque = float('-inf')
        for i in range(num_gears):
            a, b, c = map(int, input().split())
            x = find_x_coord(-a, b)
            y = find_y_coord(-a, b, c, x)
            if y > max_torque:
                max_torque = y
                max_torque_gear = i + 1
        print(max_torque_gear)


if __name__ == '__main__':
    main()
