def unique_chars_in_string(input_string):
    dictionary = {}
    for c in input_string:
        if c not in dictionary:
            dictionary[c] = 1
        else:
            return False
    return True

print(unique_chars_in_string('aa'))