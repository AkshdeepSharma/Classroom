def find_partitions(input_list):
    answer = []
    lower = input_list[0]
    upper = input_list[0]
    for num in input_list[1:]:
        if num == upper + 1:
            upper = num
        elif lower == upper:
            answer.append(upper)
            lower = upper = num
        else:
            answer.append("%d-%d" % (lower, upper))
            lower = upper = num
    if lower == upper:
        answer.append(upper)
    else:
        answer.append("%d-%d" % (lower, upper))
    return answer


input_list = [1, 2, 3, 6, 7, 8, 10, 11]
print(find_partitions(input_list))
