def binary_search(array, target):
    lower, upper = 0, len(array) - 1

    while lower <= upper:
        mid = (lower + upper) // 2
        if array[mid] < target:
            lower = mid + 1
        elif array[mid] > target:
            upper = mid + 1
        else:
            return mid
    return None
