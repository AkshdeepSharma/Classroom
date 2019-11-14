def find_best_day(space_junk):
    best_day = least_junk = float('inf')
    for i, val in enumerate(space_junk):
        if val < least_junk:
            least_junk = val
            best_day = i
    return best_day


def main():
    num_days = int(input())
    space_junk = list(map(int, input().split()))
    print(find_best_day(space_junk))


if __name__ == "__main__":
    main()
