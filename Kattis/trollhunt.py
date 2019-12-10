def find_troll(num_bridges, num_knights, knights_per_group):
    total_groups = num_knights // knights_per_group
    days = num_bridges // total_groups
    remainder = num_bridges % total_groups
    if days == num_bridges:
        return days - 1
    if remainder <= 1:
        return days
    return days + 1


def main():
    num_bridges, num_knights, knights_per_group = map(int, input().split())
    print(find_troll(num_bridges, num_knights, knights_per_group))


if __name__ == '__main__':
    main()
