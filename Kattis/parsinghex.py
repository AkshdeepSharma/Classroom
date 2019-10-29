hex_numbers = []
try:
    while True:
        line = input()
        if line == "0":
            break
        for i in range(len(line) - 2):
            if line[i] == "0" and line[i + 1].lower() == "x":
                append_index = i
                i += 2
                while True:
                    try:
                        if int(line[append_index: i + 1], 16):
                            i += 1
                            continue
                    except (IndexError, ValueError):
                        break
                hex_numbers.append(line[append_index:i])
except EOFError:
    pass

for i in range(len(hex_numbers)):
    print(hex_numbers[i], int(hex_numbers[i], 16))
