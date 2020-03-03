def maxTasksCanBeCompleted(time, tasks):
    curr_time, tasks_completed = 0, 0
    for task in tasks:
        if curr_time + task > time:
            break
        curr_time += task
        tasks_completed += 1
    return tasks_completed


def main():
    num_tasks, time = map(int, input().split())
    tasks = list(map(int, input().split()))
    print(maxTasksCanBeCompleted(time, tasks))


if __name__ == "__main__":
    main()
