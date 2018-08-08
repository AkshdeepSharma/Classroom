# Book Solution


def can_reach_end(A):
    furthest_reached_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reached_so_far < last_index:
        furthest_reached_so_far = max(furthest_reached_so_far, A[i] + i)
        i += 1
    return furthest_reached_so_far >= last_index


print(can_reach_end([3, 3, 1, 0, 2, 0, 1]))


# My Solution


def array_advancement(A):
    furthest_travelled = 0
    total_distance = len(A) - 1
    i = 0
    while i <= furthest_travelled < total_distance:
        furthest_travelled = max(furthest_travelled, A[i] + i)
        i += 1
    return furthest_travelled >= total_distance

