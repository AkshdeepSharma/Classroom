def triple_sum(integer_list, target_number):
    answer = []
    for i in range(len(integer_list) - 2):
        l = i + 1
        r = len(integer_list) - 1
        while l < r:
            if (integer_list[i] + integer_list[l] + integer_list[r]) == target_number:
                if tuple((integer_list[i], integer_list[l], integer_list[r])) not in answer:
                    answer.append(tuple((integer_list[i], integer_list[l], integer_list[r])))
                l += 1
            elif (integer_list[i] + integer_list[l] + integer_list[r]) < target_number:
                l += 1
            else:
                r -= 1
    return answer