def decode_string(msg):
    if len(msg) == 0:
        return 0
    previous_ways = 0
    possible_ways = 1
    for i in range(len(msg)):
        if not msg[i].isdigit():
            return 0
        temp = 0
        if msg[i] != "0":
            temp = possible_ways
        if i > 0 and int(msg[i - 1:i + 1]) <= 26 and msg[i - 1] != 0:
            temp += previous_ways
        previous_ways = possible_ways
        possible_ways = temp
    return possible_ways
