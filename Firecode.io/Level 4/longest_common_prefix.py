def long_common_prefix(input_list):
    same = []
    for a in zip(*input_list):
        if len(set(a)) == 1:
            same.append(a[0])
        else:
            break
    return "".join(same)