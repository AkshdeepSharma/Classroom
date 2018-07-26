def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list

    midpoint = len(a_list) // 2
    left, right = merge_sort(a_list[:midpoint]), merge_sort(a_list[midpoint:])

    return merge(left, right)


def merge(left, right):
    result = []
    left_pointer = right_pointer = 0

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result
