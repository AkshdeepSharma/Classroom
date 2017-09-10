N = int(input())
stack = []
current_max = 0
for i in range(N):
    command = input()
    if command[0] == '1':
        stack.append(int(command[1::]))
        if int(command[1::]) > current_max:
            current_max = int(command[1::])
    elif command == '2':
        if stack[-1] == current_max and current_max not in stack[:-1]:
            if len(stack) == 1:
                current_max = 0
            else:
                current_max = max(stack[:-1])
        stack.pop()
    elif command == '3':
        print(current_max)
