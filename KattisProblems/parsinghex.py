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
        while lines[k] in applicable:
            temp += lines[k]
            k += 1
        hex_numbers.append(temp)

# hex to dec
for hex in range(len(hex_numbers)):
    print(hex_numbers[hex], int(hex_numbers[hex], 16))
