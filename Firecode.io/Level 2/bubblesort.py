def bubble_sort(a_list):
    if len(a_list) == 0 or len(a_list) == 1:
        return a_list
    else:
        for i in range(len(a_list)):
            for j in range(len(a_list) - i - 1):
                if a_list[j] > a_list[j + 1]:
                    a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
    return a_list

b_list = [6,5,3,1,8,7,2,4]

print(bubble_sort(b_list))