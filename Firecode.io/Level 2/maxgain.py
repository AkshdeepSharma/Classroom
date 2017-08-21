def max_gain(input_list):
    lo = input_list[0]
    hi = 0
    for i in input_list[1:]:
        if i < lo:
            lo = i
        elif i - lo > hi:
            hi = i - lo
    return hi
