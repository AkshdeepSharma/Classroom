def main():
    total_obstacles, obstacles_found = map(int, input().split())
    set_of_obstacles_found_by_mario = set()
    for _ in range(obstacles_found):
        set_of_obstacles_found_by_mario.add(int(input()))
    for i in range(total_obstacles):
        if i not in set_of_obstacles_found_by_mario:
            print(i)
    print("Mario got " + str(len(set_of_obstacles_found_by_mario)) +
          " of the dangerous obstacles.")


if __name__ == "__main__":
    main()
