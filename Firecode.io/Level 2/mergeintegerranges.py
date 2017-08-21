input_list = [[1,10], [5,8], [8,15]]


def merge_ranges(input_range_list):
    merged_list = []
    temp_list = []
    temp_list.append(input_range_list[0][0])
    for i in range(len(input_range_list) - 1):
        if input_range_list[i][1] < input_range_list[i + 1][0]:
            temp_list.append(input_range_list[i][1])
            temp_list.append(input_range_list[i + 1][0])
    temp_list.append(input_range_list[-1][1])
    for i in range(0, len(temp_list) - 1, 2):
        mini_list = []
        mini_list.append(temp_list[i])
        mini_list.append(temp_list[i + 1])
        merged_list.append(mini_list)
    return merged_list

print(merge_ranges(input_list))