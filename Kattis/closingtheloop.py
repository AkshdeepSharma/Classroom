def close_the_loop(red, blue):
    length = 0
    strings_used = 0
    curr_colour = True
    red, blue = sorted(red), sorted(blue)
    if len(blue) == len(red):
        return sum(blue) + sum(red) - len(blue) - len(red)
    if len(red) < len(blue):
        red, blue = blue, red

    while red and blue:
        if curr_colour:
            string = red.pop()
        else:
            string = blue.pop()
        length += string
        strings_used += 1
        curr_colour = not curr_colour
    return length - strings_used


def main():
    N = int(input())
    for i in range(1, N + 1):
        blue = []
        red = []
        S = int(input())
        all_strings = input().split()
        for string in all_strings:
            if string[-1] == 'R':
                red.append(int("".join(list(string)[:-1])))
            else:
                blue.append(int("".join(list(string)[:-1])))
        final_length = close_the_loop(red, blue)
        print("Case #" + str(i) + ": " + str(final_length))


if __name__ == '__main__':
    main()
