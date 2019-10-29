N = int(input())
events_stack = []
events_dict = {}
for _ in range(N):
    line = input().split()
    if line[0] == "E":
        events_dict[line[1]] = len(events_stack)
        events_stack.append(line[1])
    elif line[0] == "D":
        for i in range(int(line[1])):
            event = events_stack.pop()
            events_dict.pop(event, None)
    elif line[0] == "S":
        line = line[2:]
        dream_num = len(events_stack) + 1
        dream_distance = -1
        plot_error = False
        for event in line:
            if event[0] == "!":
                if event[1:] in events_dict:
                    if events_dict[event[1:]] < dream_num:
                        dream_num = events_dict[event[1:]]
            else:
                if event not in events_dict:
                    plot_error = True
                    break
                elif dream_distance < events_dict[event]:
                    dream_distance = events_dict[event]
        if plot_error or dream_num <= dream_distance:
            print("Plot Error")
        elif dream_num == len(events_stack) + 1:
            print("Yes")
        else:
            print(str(len(events_stack) - dream_num) + " Just A Dream")
