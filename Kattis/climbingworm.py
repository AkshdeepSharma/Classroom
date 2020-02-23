def timesWormNeedsToClimb(worm_climb, worm_fall, pole_height):
    curr_height = 0
    count = 0
    while True:
        curr_height += worm_climb
        count += 1
        if curr_height >= pole_height:
            break
        curr_height -= worm_fall
    return count


def main():
    worm_climb, worm_fall, pole_height = map(int, input().split())
    print(timesWormNeedsToClimb(worm_climb, worm_fall, pole_height))


if __name__ == "__main__":
    main()
