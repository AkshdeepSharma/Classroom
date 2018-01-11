hex_numbers = []
lines = []
applicable = '1234567890abcdefABCDEFxX'
# input
try:
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
except EOFError:
    pass
lines = ''.join(lines)

#  parsing
for i in range(len(lines)):
    temp = ''
    k = i
    if lines[i] == '0' and (lines[i + 1] == 'x' or lines[i + 1] == 'X'):
        try:
            while lines[k] in applicable and len(temp) <= 10:
                temp += lines[k]
                k += 1
        except IndexError:
            pass
        hex_numbers.append(temp)

# hex to dec
for i in range(len(hex_numbers)):
    print(hex_numbers[i], int(hex_numbers[i], 16))
