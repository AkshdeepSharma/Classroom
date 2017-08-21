def unique_chars_in_string(input_string):
    check = ""
    if len(input_string) == 0 or len(input_string) == 1:
        return True
    for _ in input_string:
        if _ in check:
            return False
        else:
            check += _
    return True

print(unique_chars_in_string('aa'))