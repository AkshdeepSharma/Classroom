a_stringy = "None"


def insert_star_between_pairs(a_string):
    try:
        if len(a_string) is None or len(a_string) == 1:
            return a_string
        if a_string[0] == a_string[1]:
            return a_string[0:1] + "*" + insert_star_between_pairs(a_string[1:len(a_string)])
        else:
            return a_string[0:1] + insert_star_between_pairs(a_string[1:len(a_string)])
    except TypeError:
        return None

print(insert_star_between_pairs(a_stringy))