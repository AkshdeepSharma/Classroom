N = int(input())
bus_numbers = sorted(list(map(int, input().split())))
res = [str(bus_numbers[0])]

for i in range(1, len(bus_numbers) - 1):
    if (bus_numbers[i - 1] == "-" or bus_numbers[i - 1] + 1 == bus_numbers[i]) and bus_numbers[i + 1] - 1 == bus_numbers[i]:
        if bus_numbers[i - 1] == "-":
            bus_numbers[i] = "-"
            continue
        else:
            bus_numbers[i] = "-"
            res.append("-")
    else:
        if bus_numbers[i - 1] == "-":
            res += [str(bus_numbers[i])]
        else:
            res += [" ", str(bus_numbers[i])]

if res[-1] == "-":
    print("".join(res + [str(bus_numbers[-1])]))
else:
    print("".join(res + [" ", str(bus_numbers[-1])]))
