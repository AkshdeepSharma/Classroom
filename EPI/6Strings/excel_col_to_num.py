# My Solution


def col_to_num(col_name):
    col_to_num_dict = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }

    col_num = 0
    for i in reversed(range(len(col_name))):
        col_num += 26 ** (len(col_name) - i - 1) * (col_to_num_dict.get(col_name[i]))
        print(i, len(col_name), col_to_num_dict.get(col_name[i]))
    return col_num


# Book Solution
import functools


def ss_decode_col_id(col):
    return functools.reduce(lambda result, c: result * 26 + ord(c) - ord('A') + 1, col, 0)

