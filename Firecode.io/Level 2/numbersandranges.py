class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"


def find_range(input_list, input_number):
    output = Range(input_list.index(input_number), 0)
    for i in range(len(input_list)):
        if input_list[i] == input_number:
            output.upper_bound = i
    return output

# supposed to solve with logn bigO
