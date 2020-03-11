def findHexNumbers(line):
    ans = []
    valid_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}
    start_indices = [i + 2 for i in range(len(line)) if line.startswith(
        '0x', i) or line.startswith('0X', i)]
    for index in start_indices:
        for i in range(index, len(line)):
            if line[i] not in valid_chars:
                ans.append(line[index - 2: i])
                break
    for hexNum in ans:
        yield (hexNum, str(int(hexNum[2:], 16)))


def main():
    try:
        while True:
            line = input()
            ans = list(findHexNumbers(line))
            for pair in ans:
                print(pair[0] + " " + pair[1])
    except EOFError:
        pass


if __name__ == "__main__":
    main()
