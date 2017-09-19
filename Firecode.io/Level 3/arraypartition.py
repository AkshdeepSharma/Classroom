def find_partitions(input_list):
    answer = []
    if input_list is None or len(input_list) == 0:
        return answer
    if input_list == 1:
        answer.append(str(input_list[0]))
    previous = input_list[0]
    first = previous
    i = 1
    while i < len(input_list):
        if input_list[i] == previous + 1:
            if i == len(input_list) - 1:
                answer.append(str(first) + '-' + str(input_list[i]))
        else:
            if first == previous:
                answer.append(str(first))
            else:
                answer.append(str(first) + '-' + str(previous))
            if i == len(input_list) - 1:
                answer.append(str(input_list[i]))
            first = input_list[i]
        previous = input_list[i]
        i += 1
    return answer


input_list = [1, 2, 3, 6, 7, 8, 10, 11]
print(find_partitions(input_list))
