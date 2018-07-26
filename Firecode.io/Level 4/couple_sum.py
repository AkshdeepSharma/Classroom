def couple_sum(number_list, target):
    dict = {}
    for i in range(len(number_list)):
        if number_list[i] in dict:
            return [dict[number_list[i]] + 1, i + 1]
        else:
            dict[target - number_list[i]] = i
    return None
