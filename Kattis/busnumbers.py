def busnumbers(bus_numbers):
    res = [bus_numbers[0]]
    for i in range(1, len(bus_numbers) - 1):
        if bus_numbers[i] - 1 == bus_numbers[i - 1] and bus_numbers[i] + 1 == bus_numbers[i + 1]:
            if res[-1] == "-":
                continue
            res.append('-')
        else:
            if res[-1] == "-":
                res.append(bus_numbers[i])
            else:
                res += [" ", bus_numbers[i]]
    if res[-1] == "-":
        res.append(bus_numbers[-1])
    else:
        res += [" ", bus_numbers[-1]]
    return "".join(map(str, res))


def main():
    N = int(input())
    bus_numbers = sorted(list(map(int, input().split())))
    print(busnumbers(bus_numbers))


if __name__ == "__main__":
    main()
