try:
    while True:
        inp = input().split()
        N, M = int(inp[0]), int(inp[1])
        set_data, sum_set_data, elements = {}, {}, {}

        for i in range(1, N + 1):
            set_data[i] = i
            sum_set_data[i] = i
            elements[i] = [i]
        
        for _ in range(M):
            inp = input().split()
            command = int(inp[0])
            if command == 1:
                num1, num2 = int(inp[1]), int(inp[2])
                if set_data[num1] != set_data[num2]:
                    if len(elements[set_data[num1]]) <= len(elements[set_data[num2]]):
                        mini, maxi = set_data[num1], set_data[num2]
                    else:
                        mini, maxi = set_data[num2], set_data[num1]
                    elements[maxi].extend(elements[mini])
                    for element in elements[mini]:
                        set_data[element] = maxi
                    elements[mini] = []
                    sum_set_data[maxi] += sum_set_data[mini]
                    sum_set_data[mini] = 0

            elif command == 2:
                num1, num2 = int(inp[1]), int(inp[2])
                if set_data[num1] != set_data[num2]:
                    elements[set_data[num2]].append(num1)
                    sum_set_data[set_data[num2]] += num1
                    sum_set_data[set_data[num1]] -= num1
                    elements[set_data[num1]].pop(elements[set_data[num1]].index(num1))
                    set_data[num1] = set_data[num2]

            else:
                num = int(inp[1])
                print(str(len(elements[set_data[num]])), str(sum_set_data[set_data[num]]))
except EOFError:
    pass