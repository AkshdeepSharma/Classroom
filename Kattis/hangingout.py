def count_people_on_terrace(max_people, events):
    curr_people = groups_rejected = 0
    for i in range(len(events)):
        if events[i][0] == "enter":
            if int(events[i][1]) + curr_people > max_people:
                groups_rejected += 1
            else:
                curr_people += int(events[i][1])
        else:
            curr_people -= int(events[i][1])
    return groups_rejected


def main():
    max_people, num_events = map(int, input().split())
    events = [input().split() for _ in range(num_events)]
    print(count_people_on_terrace(max_people, events))


if __name__ == '__main__':
    main()
