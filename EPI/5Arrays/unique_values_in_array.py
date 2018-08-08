# Book Solution


def delete_duplicates(A):
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[write_index - 1] != A[i]:
            A[write_index] = A[i]
            write_index += 1
    return write_index


# My Solution


def unique_values_in_array(A):
    if not A:
        return 0
    unique_values = 1
    current = A[0]
    for i in range(1, len(A)):
        if A[i] != current:
            current = A[i]
            unique_values += 1
    return unique_values


print(unique_values_in_array([2,3,5,5,7,11,11,11,13]))